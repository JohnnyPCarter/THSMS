from queue import Empty, PriorityQueue
from types import NoneType
import cv2 
import numpy as np
import os
from collections import deque
from datetime import datetime

capture = cv2.VideoCapture(0)
count = 0
frameCount = 0
fileNumber = 0
countdown = 0
countdown2 = 0
DEFAULT_FILE_NAME = "/var/www/html/event"

# Define the codec and create VideoWriter object
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

photoQueue1 = deque()
photoQueue6 = deque()
photoQueue12= deque()
photoQueue24= deque()


fourcc = cv2.VideoWriter_fourcc(*'XVID')




if not capture.isOpened():
    print("Error: Coupld not open camera")
    exit()

fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)

x1, y1, x2, y2 = 100, 100, 700, 700
l1, w1, l2, w2 = 800, 100, 1400, 700


while(1):
    ret, frame = capture.read()

    if not ret:
        print("could not open frame")
        break

    frameCount += 1

    roi1 = frame[y1:y2, x1:x2]

    roi2 = frame[l1:l2, w1:w2]

    cv2.rectangle(roi1, (0,0), (700,700), (255,0,0), 2)

    fgmask = fgbg.apply(roi1)
    fgmaskRoi2 = fgbg.apply(roi2)

    count = np.count_nonzero(fgmask)
    countRoi2 = np.count_nonzero(fgmaskRoi2)


    currTime = datetime.now()

    if (frameCount > 3 and count > 5000):
        if countdown == 0:
            temp = "event" + str(fileNumber)
            output_dir = os.path.join(DEFAULT_FILE_NAME, temp)
            os.makedirs(output_dir, exist_ok=True)
            video_filename = os.path.join(output_dir, 'video.mp4')
            out = cv2.VideoWriter(video_filename, fourcc, 24.0, size)
            timer1 = (currTime, output_dir)
            timer2 = (currTime, output_dir)
            timer3 = (currTime, output_dir)
            timer4 = (currTime, output_dir)
            photoQueue1.append(timer1)
            photoQueue6.append(timer2)
            photoQueue12.append(timer3)
            photoQueue24.append(timer4)
            print("event" + str(fileNumber) + " -- ROI1 -- frameCount: " + frameCount )

            fileNumber += 1

        countdown = 120

    if (frameCount > 3 and countRoi2 > 5000):
        if countdown2 == 0:
            temp = "event" + str(fileNumber)
            output_dir = os.path.join(DEFAULT_FILE_NAME, temp)
            os.makedirs(output_dir, exist_ok=True)
            video_filename = os.path.join(output_dir, 'video.mp4')
            out2 = cv2.VideoWriter(video_filename, fourcc, 24.0, size)
            timer1 = (currTime, output_dir)
            timer2 = (currTime, output_dir)
            timer3 = (currTime, output_dir)
            timer4 = (currTime, output_dir)
            photoQueue1.append(timer1)
            photoQueue6.append(timer2)
            photoQueue12.append(timer3)
            photoQueue24.append(timer4)
            print("event" + str(fileNumber) + " -- ROI2 -- frameCount: " + frameCount )
            fileNumber += 1

        countdown2 = 120
    

    

    if countdown > 0:
        out.write(frame)

    if countdown == 1:
        out.release()
        print("releasing ROI1")


    if countdown > 0:
        print(str(countdown) + " ROI1")
        countdown -= 1

    if countdown2 > 0:
        out2.write(frame)

    if countdown2 == 1:
        out2.release()
        print("releasing ROI2")


    if countdown2 > 0:
        print(str(countdown2) + " ROI2")
        countdown2 -= 1


    
    #3600
    if (len(photoQueue1) > 0 and (currTime - photoQueue1[0][0]).total_seconds() >= 3):
        photoName = os.path.join(photoQueue1[0][1], 'hour1.png')
        cv2.imwrite(photoName, frame)
        photoQueue1.popleft()

    #21600
    if (len(photoQueue6) > 0 and (currTime - photoQueue6[0][0]).total_seconds() >= 10):
        photoName = os.path.join(photoQueue6[0][1], 'hour6.png')
        cv2.imwrite(photoName, frame)
        photoQueue6.popleft()

    #43200
    if (len(photoQueue12) > 0 and (currTime - photoQueue12[0][0]).total_seconds() >= 20):
        photoName = os.path.join(photoQueue12[0][1], 'hour12.png')
        cv2.imwrite(photoName, frame)
        photoQueue12.popleft()

    #86400
    if (len(photoQueue24) > 0 and (currTime - photoQueue24[0][0]).total_seconds() >= 30):
        photoName = os.path.join(photoQueue24[0][1], 'hour24.png')
        cv2.imwrite(photoName, frame)
        photoQueue24.popleft()
    
    

    k = cv2.waitKey(1) & 0xff
    if k == ord('q') or k == 27:
        break

capture.release()
out.release()
cv2.destroyAllWindows()