#!/usr/bin/node
/* a script that imports a dictionary of occurrences */

const dict = require('./101-data.js').dict;
const newDict = {};
for (const i in dict) {
  if (newDict[dict[i]] === undefined) {
    newDict[dict[i]] = [];
  }
  newDict[dict[i]].push(i);
}
console.log(newDict);
