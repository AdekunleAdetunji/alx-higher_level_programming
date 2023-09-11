#!/usr/bin/node

const argv = process.argv;
const count = argv.length;
if (count <= 3) {
  console.log(0);
} else {
  let max = Number(argv[2]);
  let max1 = Number(argv[2]);
  for (let i = 2; i < count; i++) {
    if (Number(argv[i]) > max) {
      max1 = max;
      max = Number(argv[i]);
    } else if (Number(argv[i]) > max1) {
      max1 = Number(argv[i]);
    }
  }
  console.log(max1);
}
