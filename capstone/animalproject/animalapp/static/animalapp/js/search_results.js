/**
 * Created by polina on 8/9/17.
 */

'use strict';

//submits form on change of the drop-down filter lists dynamically
$(function() {
  $('#filters').on('change', function(e) {
    $(this).closest('form')
           .trigger('submit')
  })
});