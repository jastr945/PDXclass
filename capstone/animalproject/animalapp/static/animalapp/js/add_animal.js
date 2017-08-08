/**
 * Created by polina on 8/1/17.
 */


// Opens the 'add animal' form form upon clicking
$('#addOption').click(function (e) {
    e.preventDefault();
    $('#addAnimal').toggle('fast')
});


// Depending on selection choice, shows either dog or cat form to fill out
$(function() {
    $('#id_species').change(function () {
        if ($(this).val() === 'dog') {
            $('.cat').hide();
            $('.dog').show();
        } else if ($('#id_species').val() === 'cat') {
            $('.dog').hide();
            $('.cat').show();
        } else {
            $('.dog').hide();
            $('.cat').hide();
        }
    });
});


// Opens the list of database entries upon clicking
$('#seeAllOption').click(function (e) {
    e.preventDefault();
    $('#tableContainer').slideToggle('fast');
});


//Shows the bar with deletion choices
$('.delete').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        $(this).parent().parent().siblings('.deleteEntry').show();
    });
});


//Hides the bar with deletion choices
$('.noDelete').each(function () {
    $(this).click(function (e) {
        e.preventDefault();
        $(this).parents('.deleteEntry').hide();
    });
});