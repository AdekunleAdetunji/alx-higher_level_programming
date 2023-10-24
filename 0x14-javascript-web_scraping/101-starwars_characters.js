#!/usr/bin/node
/*
A script that prints all characters of a Star Wars movie using the starwars API
*/

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

function reqCallback (err, response, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    const charIdx = 0;

    function recursion (chars, charIdx) {
      request.get(chars[charIdx], (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
          if (charIdx++ < chars.length) {
            recursion(chars, charIdx++);
          }
        }
      });
    }

    recursion(chars, charIdx);
  }
}

request.get(url, reqCallback);
