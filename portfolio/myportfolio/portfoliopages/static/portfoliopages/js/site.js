/**
 * Created by polina on 7/16/17.
 */
'use strict';

//slides from one part of the main page to another upon click
$('#arrow').click(function () {
    $('#titlePageTable').slideUp(300, 'swing', function () {
        $("#mainContainer").appendTo('#firstContainer').css('display', 'flex');
        $('#firstContainer').css('overflow', 'auto');
    });
});

//shows up project view options upon click, only when the project options bar is hidden
$('.project').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        if ($(this).find('.arrowClose').is(':hidden')) {
            $(this).children('.projectButtons').slideDown({duration: "fast"})
        }
    })
});

//hides project view options upon click
$('.arrowClose').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        $(this).parents('.projectButtons').slideUp({duration: "fast"});
    })
});

//shows email info upon click
$('#gMail').click(function (e) {
    e.preventDefault();
    $('#tip').show({duration: "fast"});
    $('#tooltip').show({duration: "fast"});
});

//copies email address to clipboard
$(document).ready(function () {
    var clipboard = new Clipboard('#copy');
    clipboard.on('success', function(e) {
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);
    $('#copy').css('background-color', '#2b353a');

    e.clearSelection();
    });
});
