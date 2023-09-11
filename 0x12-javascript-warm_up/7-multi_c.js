#!/usr/bin/node

const str = 'C is fun';
const count = Number(process.argv[2]);
if (count) {
  for (let i = 0; i < count; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
