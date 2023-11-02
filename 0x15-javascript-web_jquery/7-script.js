#!/usr/bin/node
/*
A JavaScript script that fetches the character name from this URL:
https://swapi-api.alx-tools.com/api/people/5/?format=json
*/
function result (data) {
  $('DIV#character').text(data.name);
}
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  result);
