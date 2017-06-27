function insertPic () {
    if (data['weather']['id'] === '500') {
        $('.content').css('background-image', 'url(rain.jpg)');
    } else if (data['weather']['id'] === '500') {
        $('.content').css('background-image', 'url(sun.jpg)')
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
            }

        });
}


$('#checkWeather').click(getWeather);