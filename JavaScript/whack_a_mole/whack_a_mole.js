var score = 0;
var t = 0;
var myTimer;
var myInterval; //making this variable available for other functions


//uses a random number to inject a picture of a mole into a div with a corresponding id number
function pickHole () {
    var holeNumber = (Math.floor(Math.random() * 20) + 1);
    $('#' + holeNumber).html("<img src='mole.jpg'/>").addClass('active');

    //changes image back to a hole and adds score points ONLY when the image on a mole is on
    $('#' + holeNumber).click(function () {
        if ($(this).attr('class') === 'active') {
            $(this).html("<img src='hole.jpg'/>").removeClass('active');
            score++;
            $('#scoreCounter').html(score);
        }
    });
}

//makes moles appear every second and starts counting the time upon clicking the 'start game' button
$('#start').click(function () {
    myTimer = setInterval(function () {
        $('#timeCounter').html(t);
        t++;},1000);

    myInterval = setInterval(pickHole, 1000);
    pickHole();
});

//stops the counter upon clicking the button and resumes the counter upon clicking the button the second time
$('#stop').click(function () {
    $(this).toggleClass('active');
    if ($(this).attr('class') === 'active') {
        $(this).html('RESUME');
        clearInterval(myInterval);
            } else {
        $('#stop').html('STOP');
        myInterval = setInterval(pickHole, 1000);
        pickHole();
    }
});

// sets score to none, stops the counter and resets all images to holes
$('#reset').click(function () {
    clearInterval(myInterval);
    clearInterval(myTimer);
    $('#scoreCounter').html(0);
    $( "#row1" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row2" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row3" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row4" ).find('*').html("<img src='hole.jpg'/>");
    $('#stop').removeClass('active').html('STOP');
});

