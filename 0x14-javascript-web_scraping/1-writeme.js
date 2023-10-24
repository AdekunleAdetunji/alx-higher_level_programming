#!/usr/bin/node

/*
This module write the second argument string supplied on the shell to the path
string supplied as first argument to the script
*/

const fs = require('fs');

function callback (err, data) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(process.argv[2], process.argv[3], 'utf8', callback);
