function insertPic (someid) {
    if (someid >= 200 && someid < 300) {
        $('#body').css({'background-image': 'url(thunderstorm.jpg)'});
        $('#icon').append("<img src='4.png'/>");
    } else if (someid >= 300 && someid <= 531) {
        $('#body').css({'background-image': 'url(rain.jpg)'});
        $('#icon').append("<img src='3.png'/>");
    } else if (someid >= 600 && someid <= 622) {
        $('#body').css({'background-image': 'url(snow.jpeg)'});
        $('#icon').append("<img src='5.png'/>");
    } else if (someid >= 701 && someid <= 781) {
        $('#body').css({'background-image': 'url(fog.jpg)'});
        $('#icon').append("<img src='6.png'/>");
    } else if (someid === '800') {
        $('#body').css('background-image', 'url(sun.jpg)');
        $('#icon').append("<img src='1.png'/>");
    } else if (someid >= 801 && someid <= 804) {
        $('#body').css('background-image', 'url(clouds.jpg)');
        $('#icon').append("<img src='2.png'/>");
    } else if (someid >= 900 && someid <= 962) {
        $('#body').css('background-image', 'url(warning.jpg)');
    }
}

function getWeather () {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            APPID: '6b919e5d511686a6a70d2728794a6fe5',
            q: $('#city').val()
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            $('#result').append('Weather: ' + data['weather'][0]['description'] + '<br/>' + 'Temperature: ' +
                Math.round((data['main']['temp'] * 9/5 - 459.67)).toFixed(2) + 'F' + '<br/>' +
                'Wind: ' + data['wind']['speed'] + 'm/s' + '<br/>' + 'Humidity: ' + data['main']['humidity']
            + '%' + '<br/>' + 'Pressure: ' + data['main']['pressure'] + 'hpa');
            var weatherId = data['weather'][0]['id'].toString();
            insertPic(weatherId)
            }

        });
}

$('#checkWeather').click(getWeather);