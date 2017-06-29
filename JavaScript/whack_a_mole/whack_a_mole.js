var score  = 0;


//uses a random number to inject a picture of a mole
function pickHole () {
    var holeNumber = (Math.floor(Math.random() * 20) + 1);
    $('#' + holeNumber).html("<img src='mole.jpg'/>");
}

var myInterval = setInterval(pickHole, 1000);

$('#' + holeNumber).click(function () {
    $('#' + holeNumber).html("<img src='hole.jpg'/>");
    score++;
    $('#timer').html(score);
});


$('#start').click(function () {
    pickHole();
});

//stops the counter upon clicking the button
$('#stop').click(function () {
    clearInterval(myInterval);
});

// sets score to none, stops the counter and resets all images to holes
$('#reset').click(function () {
    clearInterval(myInterval);
    $('#timer').html('-');
    $( "#row1" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row2" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row3" ).find('*').html("<img src='hole.jpg'/>");
    $( "#row4" ).find('*').html("<img src='hole.jpg'/>");
});

