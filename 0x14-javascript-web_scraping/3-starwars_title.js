#!/usr/bin/node
/*
This module uses the request module to communicate with the
https://swapi-api.alx-tools.com/api/films/:id api and prints the movie
title to stdout
*/

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request.get(url, (error, response, body) => {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
