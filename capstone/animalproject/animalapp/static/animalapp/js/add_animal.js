/**
 * Created by polina on 8/1/17.
 */


// Opens the 'add animal' form form upon clicking
$('#addOption').click(function (e) {
  e.preventDefault();
  $('#addAnimalTable').toggle('fast')
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

// JQuery form validation
$(document).ready(function() {
    $('form').validate({
      rules:
      {
        name:
        {
          required: true,
        },
        id_number:
        {
          required: true,
        },
        species:
        {
          required: true,
        },
        birthday:
        {
          required: true,
        },
        cat_color:
        {
          required: true,
        },
        cat_personality:
        {
          required: true,
        },
        dog_breed:
        {
          required: true,
        },
        size:
        {
          required: true,
        },
        dog_personality:
        {
          required: true,
        },
        dog_color:
        {
          required: true,
        },
      },
      submitHandler: function(form)
      {
        form.submit();
      }
  });
});

// Opens the list of database entries upon clicking
$('#seeAllOption').click(function (e) {
  e.preventDefault();
  $('#tableContainer').slideToggle('fast');
});


// Submits form on change of the drop-down filter lists dynamically
$(function() {
  $('#dbfilters').on('change', function (e) {
    e.preventDefault();
    $(this).submit()
  })
});


// Shows the bar with deletion choices
$('.delete').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    $(this).parent().parent().siblings('.deleteEntry').show();
  });
});


// Hides the bar with deletion choices
$('.noDelete').each(function () {
  $(this).click(function (e) {
      e.preventDefault();
      $(this).parents('.deleteEntry').hide();
  });
});


// Shows the edit form upon clicking the specific edit button
$('.edit').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    $(this).parent().parent().parent().next('.editProfile').show();
  });
});


// Hides the edit form upon clicking the cross icon
$('.cross').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    $(this).parent('.editProfile').hide();
  });
});


// Removes a picture from the list upon clicking on the cross icon
$('.deleteIMG').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    var photo = $(this).parent('.photos');
    var href = $(this).attr("href");
    $.ajax({
      url: href,
      type: "GET",
      success: function (e) {
        console.log(photo);
        photo.fadeOut("fast");
      }
    });
  });
});
