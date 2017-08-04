/**
 * Created by polina on 8/1/17.
 */

// Opens the 'add animal' form upon clicking
$('#addOption').click(function (e) {
    e.preventDefault();
    $('#addAnimal').toggle('fast')
});

$('#seeAllOption').click(function (e) {
    e.preventDefault();
    $('#tableContainer').slideToggle('fast')
});

// Depending on selection choice, shows either dog or cat form to fill out
$(function() {
    $('#id_species').change(function () {
        if ($('#id_species').val() === 'dog') {
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

