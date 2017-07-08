/**
 * Created by polina on 7/6/17.
 */
'use strict';

var total = 6.00;

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
        $('.ui.relaxed.list > li:contains('+ ingredient +')').remove()
    }
});

// manages the checkbox buttons of the 'included-ingredients' section
$('[type=checkbox][name=included-ingredients]').change(function() {
    var ingredient = $(this).next().text();
    if (this.checked) {
        $('.ui.relaxed.list').append('<li class="item">'+ ingredient + '</li>')
    } else {
        $('.ui.relaxed.list > li:contains('+ ingredient +')').remove()
    }
});

// manages the checkbox buttons of the 'extra-ingredients' section; adds or extracts extra cost from the total
$('[type=checkbox][name=extra-ingredients]').change(function() {
    var ingredient = $(this).next().text();
    if (this.checked) {
        $('.ui.relaxed.list').append('<li class="item">'+ ingredient + '</li>');
        total = total + 0.50;
        $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
    } else {
        $('.ui.relaxed.list > li:contains('+ ingredient +')').remove();
        total = total - 0.50;
        $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
    }
});


// adds delivery cost to the total only when the radio button 'delivery' is selected;
$('[type=radio][value=delivery]').on('change', function () {
    if ($(this).hasClass('costAdded')) {
            total = total + 0.00;
            $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
    } else {
        total = total + 5.00;
        $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
        $(this).addClass('costAdded');
        $('[type=radio][value=pick-up]').removeClass('costAdded');
    }
});

// extracts delivery cost from the total only when the radio button 'pick-up' is selected;
$('[type=radio][value=pick-up]').on('change', function () {
    if ($(this).hasClass('costAdded')) {
            total = total + 0.00;
            $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
    } else {
        total = total - 5.00;
        $('#total_cost').html('<strong>' + 'Total: ' + '</strong>' + '$' + total.toFixed(2));
        $(this).addClass('costAdded');
        $('[type=radio][value=delivery]').removeClass('costAdded');
    }
});



//form validation