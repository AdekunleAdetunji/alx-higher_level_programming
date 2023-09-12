#!/usr/bin/node

/*
This module contains a rectangle class that defines a class with the
constructor taking two arguments (w, h)
*/
const Rectangle = require('./5-square');
const Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
module.exports = Square;
