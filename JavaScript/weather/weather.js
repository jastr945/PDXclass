function insertPic (someid) {
    if (someid >= 200 && someid < 300) {
        $('.content').css({'background-image': 'url(thunderstorm.jpg)'});
    } else if (someid >= 300 && someid <= 531) {
        $('.content').css({'background-image': 'url(rain.jpg)'});
    } else if (someid >= 600 && someid <= 622) {
        $('.content').css({'background-image': 'url(snow.jpeg)'});
    } else if (someid >= 701 && someid <= 781) {
        $('.content').css({'background-image': 'url(fog.jpg)'});
    } else if (someid === '800') {
        $('.content').css('background-image', 'url(sun.jpg)');
    } else if (someid >= 801 && someid <= 804) {
        $('.content').css('background-image', 'url(clouds.jpg)');
    } else if (someid >= 900 && someid <= 962) {
        $('.content').css('background-image', 'url(warning.jpg)');
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
            $('#result').append('Weather: ' + data['weather'][0]['description'] + '<br/>' + 'Temperature: ' + data['main']['temp'] + '<br/>' +
                'Wind: ' + data['wind']['speed'] + '<br/>' + 'Humidity: ' + data['main']['humidity']
            + '<br/>' + 'Pressure: ' + data['main']['pressure']);
            var weatherId = data['weather'][0]['id'].toString();
            insertPic(weatherId)
            }

        });
}

$('#checkWeather').click(getWeather);