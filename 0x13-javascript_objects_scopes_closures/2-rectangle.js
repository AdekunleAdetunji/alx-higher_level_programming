#!/usr/bin/node

/*
This module contains a rectangle class that defines a class with the
constructor taking two arguments (w, h)
*/
const Rectangle = class Rectangle {
    constructor(w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	};
    };
};
module.exports = Rectangle
