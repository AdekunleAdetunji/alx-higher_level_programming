#!/usr/bin/node
/*
This is a script that prints the number of movies where the character
 “Wedge Antilles” is present.
*/

const request = require('request');

function reqCallback (er, response, body) {
  console.log(JSON.parse(body).films.length);
}

request.get('https://swapi-api.alx-tools.com/api/people/18/', reqCallback);
