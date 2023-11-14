#!/usr/bin/node
/* This concatenates two files */

const args = process.argv.slice(2);
const fs = require('fs');
const firstFile = fs.readFileSync('./' + args[0]);
const secondFile = fs.readFileSync('./' + args[1]);
fs.writeFileSync('./' + args[2], firstFile + secondFile);
