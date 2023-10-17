# THSMS

Here's the deal:
This project uses openCV in python in order to create regions of interest (ROI) and track changes in them. If there is a change in the ROI compared to the general history of the ROI, it takes a video. Then it takes a photo 1 hour, 6 hours, 12 hours, and 24 hours after the original video. It logs this in a sqlite database through Flask. 
This is viewable through the web interface. Javascript is used to generate a webpage so you can look through the history of the ROI.