#!/usr/bin/node

const argvec = process.argv;

if (argvec[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argvec[2]);
}
