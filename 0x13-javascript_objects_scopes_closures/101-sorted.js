#!/usr/bin/node
/* This imports a dictionary of occurrences by user id and also computes it by user id */

const dict = require('./101-data.js').dict;
const outDict = {};
for (const I in dict) {
  if (outDict[dict[I]] === undefined) {
    outDict[dict[I]] = [];
  }
  outDict[dict[I]].push(I);
}
console.log(outDict);
