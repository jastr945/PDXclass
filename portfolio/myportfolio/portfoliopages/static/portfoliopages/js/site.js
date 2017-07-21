/**
 * Created by polina on 7/16/17.
 */
'use strict';

//makes a slide from one part of the main page to another upon click
$('#arrow').click(function () {
    $('#titlePageTable').slideUp(300, 'swing', function () {
        $("#mainContainer").appendTo('#firstContainer');
    });
});

//shows up project view options upon click, only when the project options bar is hidden
$('.project').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        if ($(this).find('.arrowClose').is(':hidden')) {
            $(this).children('.projectButtons').show('slow')
        }
    })
});

//hides project view options upon click
$('.arrowClose').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        $(this).parents('.projectButtons').hide('slow');
    })
});

//opens a link upon clicking on the entire div
