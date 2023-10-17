let source = "./event/";
// function to show image when we click on a image
function showImage(imageSrc) {
    let popupImage = document.getElementById("popupImage");
    popupImage.src = imageSrc;
    
    let imagePopup = document.getElementById("imagePopup");
    imagePopup.style.display = "block";
    document.body.style.overflow = "hidden";
}
    // function to hide the image when we click on cross button
function closeImage() {
    let imagePopup = document.getElementById("imagePopup");
    imagePopup.style.display = "none";
    document.body.style.overflow = "auto";
 }

function createEvent(folder) {
    const eventDiv = document.createElement('div');
    eventDiv.classList.add('event');
    eventDiv.innerHTML =   
                            '<video class="item" controls loop>' +
                            '<source src="' + source + folder +'/video.mp4" type="video/mp4" />' +
                            '</video>' +
                            '<img class="item" src="'+ source + folder +'/hour1.png" alt="">' +
                            '<img class="item" src="'+ source + folder +'/hour6.png" alt="">' +
                            '<img class="item" src="'+ source + folder +'/hour12.png" alt="">' +
                            '<img class="item" src="'+ source + folder +'/hour24.png" alt="">';
    return eventDiv;
}

const buildZone = document.getElementById('build');
function loadEvents() {
    fetch('http://localhost:5000/get_data')
        .then(response => response.json())
        .then(data => {
            data.forEach(folder => {
                const div = createEvent(folder[0]);
                console.log(div);
                buildZone.appendChild(div);
            });
        })
        .catch(error => console.error(error));
}

loadEvents();