window.onload=function(){

const text  = document.querySelector('.mainText');
const mainContainer  = document.querySelector('.container');

$(".container").on("dblclick", function(){
    var clickX = (event.layerX == undefined ? event.offsetX : event.layerX) + 1;
    var clickY = (event.layerY == undefined ? event.offsetY : event.layerY) + 1;
//    text.textContent = `MouseX: ${clickX},  MouseY: ${clickY}`;
    window.open(`/admin/mapper/workspace/add/?xPos=${clickX-20};yPos=${clickY-55}`,"_self");
});

mainContainer.addEventListener("mousemove", runEvent);
//event handler
function runEvent(e){
    e.preventDefault();
    //print Coordinates of the mouse on move on the targeted element: 
    //text.textContent = `MouseX: ${e.offsetX-20},  MouseY: ${e.offsetY-775}`;
	text.textContent = `MouseX: ${e.offsetX-20},  MouseY: ${e.offsetY-55}`;
    //change body background color taking the coordinates as values of rgb:
    //document.body.style.backgroundColor = `rgb(${e.offsetX}, 180, ${e.offsetY})`;
}
}