#!/usr/bin/node
/* A script that prints x times “C is fun” */

const args = Number(process.argv[2]);
let i;
if (args) {
  for (i = 0; i < args; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
