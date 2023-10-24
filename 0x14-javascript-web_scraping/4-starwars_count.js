#!/usr/bin/node
/*
This is a script that prints the number of movies where the character
 “Wedge Antilles” is present.
*/

const request = require('request');

function reqCallback (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
}
request.get(process.argv[2], reqCallback);
