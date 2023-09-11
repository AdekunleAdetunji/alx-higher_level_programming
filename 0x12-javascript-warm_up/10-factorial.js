#!/usr/bin/node

const number = Number(process.argv[2]);
function fact (number) {
  if (!number || number < 0) {
    return 1;
  }
  return number * fact(number - 1);
}
console.log(fact(number));
