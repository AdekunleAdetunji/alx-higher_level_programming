#!/usr/bin/node
/*
A JavaScript script that toggles the class of the <header> element when the
 user clicks on the tag DIV#toggle_header using the JQuery API
*/
function toggle () {
  const header = $('header');
  if (header.hasClass('red')) {
    header.toggleClass('green');
  } else {
    header.toggleClass('red');
  }
}

$('DIV#toggle_header').on('click', toggle);
