#!/usr/bin/node
/*
A JavaScript script that updates the text color of the <header> element to
red (#FF0000) when the user clicks on the tag DIV#red_header
*/
function change () {
  const header = $('header');
  header.css('color', '#FF0000');
}

$('DIV#red_header').bind('click', change);
