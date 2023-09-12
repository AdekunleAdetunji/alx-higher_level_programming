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

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.height));
      }
    } else {
      this.print();
    }
  }
};
module.exports = Square;
