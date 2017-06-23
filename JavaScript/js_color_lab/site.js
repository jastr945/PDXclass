function setColor(somecolor) {
    document.getElementById('mybackground').style.backgroundColor = somecolor; //sets the background to some color
}

document.getElementById('setcolor').addEventListener('click', function (event) {
    event.preventDefault();
    var mycolor = document.getElementById('mycolor').value; // the color code
    setColor(mycolor);
});
