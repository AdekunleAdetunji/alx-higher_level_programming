#!/usr/bin/node

const argv = process.argv;
const count = argv.length;
if (count === 2 || count === 3) {
  console.log(0);
} else {
  let max = Number(argv[2]);
  let max1 = Number(argv[2]);
  for (let i = 0; i < count; i++) {
    if (Number(argv[i]) > max) {
      max1 = max;
      max = Number(argv[i]);
    }
  }
  console.log(max1);
}
