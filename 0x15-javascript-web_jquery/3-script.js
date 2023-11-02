#!/usr/bin/node
/*
A JavaScript script that adds the class red to the <header> element when the
 user clicks on the tag DIV#red_header
*/
function addClass () {
  const header = $('header');
  header.addClass('red');
}

$('DIV#red_header').bind('click', addClass);
