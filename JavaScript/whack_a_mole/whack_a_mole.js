var t = 0;
var inter = 1000;
var timer;
$('#start').click(function () {
    timer = setInterval(function () {
    $('#timer').html(t);
    t++;
}, inter);
});

$('#stop').click(function () {
    clearInterval(timer);
});

$('#reset').click(function () {
    clearInterval(timer);
    t=0;
    $('#timer').html('-');
});

// function Hole(id) {
//     this.id = id;
//     this.val = 0;

//picks a random number between 1 and 20
function pickHole () {
    var holeNumber = (Math.floor(Math.random() * 20) + 1).toString();
    if (holeNumber === '1') {
        $('#1').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '2') {
        $('#2').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '3') {
        $('#3').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '4') {
        $('#4').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '5') {
        $('#5').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '6') {
        $('#6').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '7') {
        $('#7').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '8') {
        $('#8').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '9') {
        $('#9').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '10') {
        $('#10').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '11') {
        $('#11').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '12') {
        $('#12').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '13') {
        $('#13').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '14') {
        $('#14').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '15') {
        $('#15').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '16') {
        $('#16').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '17') {
        $('#17').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '18') {
        $('#18').html("<img src='mole.jpg'/>");
    }  else if (holeNumber === '19') {
        $('#19').html("<img src='mole.jpg'/>");
    } else if (holeNumber === '20') {
        $('#20').html("<img src='mole.jpg'/>");
    }
}
pickHole();

//inserts an image of a hole into the div
// function makeHole() {
//     $("#field").html("<img src='mole.jpg'/>");
// }
//
// makeHole();