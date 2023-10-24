#!/usr/bin/node

/*
This module reads a file and logged the output to stdout while it prints
a custom error message when encountered
*/

const fs = require('fs');
const argv = process.argv;

function callback (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
}

fs.readFile(argv[2], 'utf8', callback);
