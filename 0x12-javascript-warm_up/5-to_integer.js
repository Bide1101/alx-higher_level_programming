#!/usr/bin/node
const args = process.argv;
const message = (args[2] % 10) ? ('My number: ' + (args[2])) : 'Not a number';
console.log(message);
