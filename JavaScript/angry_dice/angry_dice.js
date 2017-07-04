/**
 * Created by polina on 6/27/17.
 */
/**
 * Created by polina on 6/26/17.
 */
'use strict';
var round = 1;

//Creates a die object
function Die(id) {
    this.id = id;
    this.val = 0;
    this.held = false;

    //picks a random number between 1 and 6
    this.setVal = function () {
        if (!this.held) {
            this.val = (Math.floor(Math.random() * 6) + 1);
            this.render();
        }
    };

    //inserts a picture of a die depending of the random number
    this.render = function () {
        if (this.val.toString() === '1') {
            $('#' + this.id).html("<img src='1.png' height='184px' width='184px'/>");
        } else if (this.val.toString() === '2') {
            $('#' + this.id).html("<img src='2.png' height='184px' width='184px'/>");
        } else if (this.val.toString() === '3') {
            $('#' + this.id).html("<img src='3.png' height='184px' width='184px'/>");
        } else if (this.val.toString() === '4') {
            $('#' + this.id).html("<img src='4.png' height='184px' width='184px'/>");
        } else if (this.val.toString() === '5') {
            $('#' + this.id).html("<img src='5.png' height='184px' width='184px'/>");
        } else if (this.val.toString() === '6') {
            $('#' + this.id).html("<img src='6.png' height='184px' width='184px'/>");
        }
    }
}

//changes the round number
function changeRound() {
    $('#roundNumber').html(round.toString());
}

//unlocks the dice, removes red border
function releaseHold() {
    die1.held = false;
    die2.held = false;
    $('#die1').css({'border-color': 'transparent',
                    'border-weight':'5px',
                    'border-style':'solid'});
    $('#die2').css({'border-color': 'transparent',
                    'border-weight':'5px',
                    'border-style':'solid'});
}

//changes round number when the conditions are met; if the value of both dice is 3, the page will reload and the game will start again.
function checkRound() {
    if (die1.val === 3 && die2.val === 3) {
        $('#message').html('Angry Dice sends you back to round 1!').css('color', 'red');
        window.setTimeout(function(){window.location.reload()}, 2000);
    } else if (round === 1 && die1.val + die2.val === 3) {
        round = 2;
        changeRound();
        releaseHold();
    } else if (round === 2 && (die1.val === 3 || die1.val === 4) && (die2.val === 3 || die2.val === 4) && die1.val + die2.val === 7) {
        round = 3;
        changeRound();
        releaseHold();
    } else if (round === 3 && die1.val + die2.val === 11) {
        $('#message').html('You WIN!!! CONGRATULATIONS!!!').css('color', 'red');
        changeRound();
        releaseHold();
    }
}

var die1 = new Die('die1');
var die2 = new Die('die2');

//rolls the dice upon clicking the button
$('#roll').click(function (e) {
    e.preventDefault();
    die1.setVal();
    die2.setVal();
    checkRound();
});

//changes the border around a die to red if it's locked
$('.dieClick').click(function () {
    if ($(this).attr('id') === 'die1' && !die1.held) {
        die1.held = true;
        $(this).css({'border-color': 'red',
                    'border-weight':'5px',
                    'border-style':'solid'});
    } else if ($(this).attr('id') === 'die1' && die1.held) {
        die1.held = false;
        $(this).css({'border-color': 'transparent',
                    'border-weight':'5px',
                    'border-style':'solid'});
    } else if ($(this).attr('id') === 'die2' && !die2.held) {
        die2.held = true;
        $(this).css({'border-color': 'red',
                    'border-weight':'5px',
                    'border-style':'solid'});
    } else if ($(this).attr('id') === 'die2' && die2.held) {
        die2.held = false;
        $(this).css({'border-color': 'transparent',
                    'border-weight':'5px',
                    'border-style':'solid'});
    }
});

//makes the welcoming message blink constantly
function blinker() {
    $('#welcome').fadeOut(500);
    $('#welcome').fadeIn(500);
}

setInterval(blinker, 1000);

//scrolls the webpage from the welcoming part to the gaming part upon clicking the button
$('#welcome').click(function () {
    $('html, body').animate({
        scrollTop: $('.dieClick').offset().top
    }, 1000);
});

//resets the game upon clicking the 'new game' button
$('#reset').click(function () {
    location.reload();
});