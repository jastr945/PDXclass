/**
 * Created by polina on 7/27/17.
 */
//This is the JavaScript/JQuery code for the index page

'use strict';

//removing placeholder from the search tab on focus and bringing it back on blur
$('#searchField').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
          .attr('placeholder','');
}).blur(function(){
   $(this).attr('placeholder', $(this).data('placeholder'));
});

