#!/usr/bin/node

/*
This module imports an array and computes a new array by multiplying it
with the array index
*/
const arr = require('./100-data.js').list;
console.log(arr);
const newArr = arr.map((x, idx) => x * idx);
console.log(newArr);
