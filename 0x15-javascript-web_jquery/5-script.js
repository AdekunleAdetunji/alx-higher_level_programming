#!/usr/bin/node

/*
A JavaScript script that adds a <li> element to a list when the user clicks
 on the tag DIV#add_item
*/

function addObject () {
  const ul = $('UL');
  ul.append('<li>Item</li>');
}

$('DIV#add_item').on('click', addObject);
