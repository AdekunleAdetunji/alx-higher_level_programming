#!/usr/bin/node

/*
This module contains a function that prints the number of argument that
have being printed and the argument itself
*/
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
