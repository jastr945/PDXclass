/**
 * Created by polina on 7/16/17.
 */
'use strict';

$('#arrow').click(function () {
    $('#titlePageTable').slideUp(300, 'swing', function () {
        $("#mainContainer").appendTo('#firstContainer');
    });
});

$('.project').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        if ($(this).find('.arrowClose').is(':hidden')) {
            $(this).children('.projectButtons').show('slow')
        }
    })
});

$('.arrowClose').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        $(this).parents('.projectButtons').hide('slow');
    })
});

$('.buttonLink').on('click', function(e) {
    e.preventDefault();

});