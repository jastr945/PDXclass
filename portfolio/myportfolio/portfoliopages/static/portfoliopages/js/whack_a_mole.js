var score = 0;
var stopTime;
var myInterval; //making this variable available for other functions

// variable counting minutes and seconds with start, pause and resume count functions
var Clock = {
  totalSeconds: 0,

  start: function () {
      var self = this;

      this.interval = setInterval(function () {
          self.totalSeconds += 1;

          $("#min").text((Math.floor(self.totalSeconds / 60 % 60)).toString() + ':');
          $("#sec").text((parseInt(self.totalSeconds % 60)).toString());
      }, 1000);

      setInterval(function (m) {

          if (self.totalSeconds >= 60) {
              clearInterval(myInterval);
              m.pause();
              $('#message').html('Game over!').css({
                  'color': 'red',
                  'font-size': '30pt'
              });
              $('#reset').css('background-color', '#FFFF14');
              $('#stop').css('background-color', '#C3C300');
          }
      }, 1000, this)
  },

  pause: function () {
    clearInterval(this.interval);
    delete this.interval;
  },

  resume: function () {
    if (!this.interval) this.start();
  }
};


//picks a random number between 1 and 20 and injects a picture of a mole into a div with a corresponding id number
//after 2 seconds, the picture of a mole turns back into a hole
function pickHole () {
    var holeNumber = (Math.floor(Math.random() * 20) + 1);
    $('#' + holeNumber).html("<img src='portfoliopages/img/mole.jpg'/>").addClass('active');
    setTimeout(function () {
        $('#' + holeNumber).html("<img src='portfoliopages/img/hole.jpg'/>").removeClass('active');
  }, 2000);

    //changes image back to a hole and adds score points ONLY when the image on a mole is on
    $('#' + holeNumber).click(function () {
        if ($(this).attr('class') === 'active') {
            $(this).html("<img src='portfoliopages/img/hole.jpg'/>").removeClass('active');
            score++;
            $('#scoreCounter').html(score);
        }
    });
}

//makes moles appear every second and starts counting time upon clicking the 'start game' button
$('#start').click(function () {
    $(this).css('background-color', '#C3C300');
    $('#stop').css('background-color', '#FFFF14');
    myInterval = setInterval(pickHole, 1000);
    Clock.start();
    pickHole();
});

//stops the counter upon clicking the button and resumes the counter upon clicking the button the second time
$('#stop').click(function () {
    $(this).toggleClass('active');
    if ($(this).attr('class') === 'active') {
        $(this).html('RESUME');
        clearInterval(myInterval);
        Clock.pause();} else {
        $('#stop').html('STOP');
        myInterval = setInterval(pickHole, 1000);
        clearInterval(stopInterval);
        pickHole();
        Clock.resume();
    }
});

// reloads the page
$('#reset').click(function () {
    location.reload(true);
});

