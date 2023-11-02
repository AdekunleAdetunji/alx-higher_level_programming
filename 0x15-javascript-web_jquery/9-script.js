#!/usr/bin/node

/*
A JavaScript script that fetches from
https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello
*/
function get (data) {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
  });
}

$('document').ready(get);
