#!/usr/bin/node

/*
This module imports an external dictionary that contains occurences by
user id and computes a dictionary of user ids by occurences
*/
const dict = require('./101-data.js').dict;
const grpDict = {};
for (const prop in dict) {
  if (grpDict[dict[prop]]) {
    grpDict[dict[prop]].push(prop);
  } else {
    grpDict[dict[prop]] = [prop];
  }
}
console.log(grpDict);
