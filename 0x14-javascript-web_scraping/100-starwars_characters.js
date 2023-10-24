#!/usr/bin/node
/*
A script that prints all characters of a Star Wars movie using the starwars API
*/

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

function reqCallback (err, response, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    for (const charUrl of chars) {
      request.get(charUrl, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
}

request.get(url, reqCallback);
