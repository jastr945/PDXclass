/**
 * Created by polina on 8/9/17.
 */

'use strict';

// enabling a slide show (PgwSlideshow JQuery plugin) for screens larger than 760px
if (window.screen.width > 780) {

  $(document).ready(function() {
      $('.pgwSlideshow').pgwSlideshow({
        autoSlide: true
      });
  });

} else {
  $(document).ready(function() {
      $('.pgwSlideshow').pgwSlideshow({
        autoSlide: false
      });
  });
};
