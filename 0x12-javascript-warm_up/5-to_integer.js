#!/usr/bin/node

const argv = process.argv;
const conv = Number(argv[2]);

if (conv) {
  console.log('My number:', conv);
} else {
  console.log('Not a number');
}
