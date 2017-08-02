/**
 * Created by polina on 8/1/17.
 */

// Depending on selection choice, shows either dog or cat form to fill out
$(function() {
    $('#id_species').change(function () {
        if ($('#id_species').val() === 'dog') {
            $('.cat').hide();
            $('.dog').show()
        } else {
            $('.dog').hide();
            $('.cat').show()
        }
    });
});
