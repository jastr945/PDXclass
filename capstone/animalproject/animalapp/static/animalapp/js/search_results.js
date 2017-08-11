/**
 * Created by polina on 8/9/17.
 */

'use strict';

//submits form on change of dropdown list
$('#id_gender').change(function () {
    $(this).form.submit()
});