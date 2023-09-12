#!/usr/bin/node

/*
This module concats two files that are supplied through the command line
to a new file supplied via the command line as well
*/
const fs = require('fs');
const argv = process.argv;
const text1 = fs.readFileSync(argv[2]);
const text2 = fs.readFileSync(argv[3]);
fs.writeFileSync(argv[4], text1 + text2);
