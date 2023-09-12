#!/usr/bin/node

/*
This module contains a function that returns the reverse of a list
*/
exports.esrever = function (list) {
  const maxIdx = list.length - 1;
  for (let i = 0; i < (maxIdx + 1) / 2; i++) {
    const temp = list[i];
    list[i] = list[maxIdx - i];
    list[maxIdx - i] = temp;
  }
  return list;
};
