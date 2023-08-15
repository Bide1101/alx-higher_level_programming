#!/usr/bin/node
/* A script that checks if the first argument can be converted to an integer */

const args = Number(process.argv[2]);
if (args) {
  console.log('My number:', args);
} else {
  console.log('Not a number');
}
