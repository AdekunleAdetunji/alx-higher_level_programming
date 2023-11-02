#!/usr/bin/node
/*
A JavaScript script that fetches and lists the title for all movies by using
this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/
function movieList (data) {
  for (const result of data.results) {
    const p = $('<li></li>').text(result.title);
    $('ul').append(p);
  }
}

$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  movieList);
