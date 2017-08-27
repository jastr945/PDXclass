// Changes a background picture of a webpage and a weather icon depending on a weather code
function insertPic (someid) {
    if (someid >= 200 && someid < 300) {
        $('#mainContainer').css({'background-image': 'url(/static/portfoliopages/img/thunderstorm.jpg)'});
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon4.png'/>");
    } else if (someid >= 300 && someid <= 531) {
        $('#mainContainer').css({'background-image': 'url(/static/portfoliopages/img/rain.jpg)'});
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon3.png'/>");
    } else if (someid >= 600 && someid <= 622) {
        $('#mainContainer').css({'background-image': 'url(/static/portfoliopages/img/snow.jpg)'});
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon5.png'/>");
    } else if (someid >= 701 && someid <= 781) {
        $('#mainContainer').css({'background-image': 'url(/static/portfoliopages/img/fog.jpg)'});
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon6.png'/>");
    } else if (someid === '800') {
        $('#mainContainer').css('background-image', 'url(/static/portfoliopages/img/sun.JPG)');
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon1.png'/>");
    } else if (someid >= 801 && someid <= 804) {
        $('#mainContainer').css('background-image', 'url(/static/portfoliopages/img/clouds.jpg)');
        $('#icon').html("<img src='/static/portfoliopages/img/weather_icon2.png'/>");
    } else if (someid >= 900 && someid <= 962) {
        $('#mainContainer').css('background-image', 'url(/static/portfoliopages/img/warning.jpg)');
    }
}

//Gets weather info(API) and extracts necessary categories from the dictionary
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
            $('#result').html('Weather: ' + data['weather'][0]['description'] + '<br/>' + 'Temperature: ' +
                Math.round((data['main']['temp'] * 9/5 - 459.67)).toFixed(2) + 'F' + '<br/>' +
                'Wind: ' + data['wind']['speed'] + 'm/s' + '<br/>' + 'Humidity: ' + data['main']['humidity']
            + '%' + '<br/>' + 'Pressure: ' + data['main']['pressure'] + 'hpa');
            $('#result').css('display', 'flex');
            var weatherId = data['weather'][0]['id'].toString();
            insertPic(weatherId)
            }
        });
}

//loads the data as a text upon clicking the button
$('#checkWeather').click(getWeather);
