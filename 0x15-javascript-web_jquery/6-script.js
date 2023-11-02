#!/usr/bin/node
/*
A JavaScript script that updates the text of the <header> element to New
Header!!! when the user clicks on DIV#update_header
*/
function update () {
  $(this).text('New Header!!!');
}
$('DIV#update_header').on('click', update);
