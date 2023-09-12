#!/usr/bin/node

/*
This module contains a rectangle class that defines a class with the
constructor taking two arguments (w, h)
*/
const Rectangle = require('./4-rectangle');
const Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = Square;
