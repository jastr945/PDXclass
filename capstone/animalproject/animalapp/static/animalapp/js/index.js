/**
 * Created by polina on 7/27/17.
 */
//This is the JavaScript/JQuery code for the index page

'use strict';

;(function(window) {

	'use strict';

	var closeCtrl = document.getElementById('btn-search-close'),
		searchContainer = document.querySelector('.search'),
		inputSearch = searchContainer.querySelector('.search__input');

	function init() {
		initEvents();
	}

	function initEvents() {
		inputSearch.addEventListener('focus', openSearch);
		closeCtrl.addEventListener('click', closeSearch);
		document.addEventListener('keyup', function(e) {
			// escape key.
			if( e.keyCode == 27 ) {
				closeSearch();
			}
		});
	}

	function openSearch() {
		searchContainer.classList.add('search--open');
		inputSearch.focus();
	}

	function closeSearch() {
		searchContainer.classList.remove('search--open');
		inputSearch.blur();
		inputSearch.value = '';
	}

	init();

})

(window);
