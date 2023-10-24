#!/usr/bin/node
/*
This module prints the status code of a request url get response
*/

const request = require('request');

function reqCallback (error, response, body) {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
}

request.get(process.argv[2], reqCallback);
