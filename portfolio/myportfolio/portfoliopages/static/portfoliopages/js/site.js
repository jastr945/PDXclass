/**
 * Created by polina on 7/16/17.
 */
'use strict';

$('#arrow').click(function () {
    $('#titlePageTable').slideUp(300, 'swing', function () {
        $("#mainContainer").appendTo('#firstContainer');
    });
});