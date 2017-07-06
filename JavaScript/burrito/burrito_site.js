/**
 * Created by polina on 7/6/17.
 */
'use strict';

// manages the radio buttons
// replaces the first element of the ingredient list with the label attached to a radio button
$('[type=radio][name=tortilla]').on('change', function () {
    $('.ui.relaxed.list > li:first-child').replaceWith('<li class="item">'+ $(this).next().text() + '</li>')
});

// manages the checkbox buttons of the 'meat' section
$('[type=checkbox][name=meat]').change(function() {
    var ingredient = $(this).next().text();
    if (this.checked) {
        $('.ui.relaxed.list').append('<li class="item">'+ ingredient + '</li>')
    } else {
        console.log(ingredient);
        $('.ui.relaxed.list > li:contains('+ ingredient +')').remove()
    }
});
