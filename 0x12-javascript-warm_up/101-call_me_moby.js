#!/usr/bin/node
/* This is a function that executes x times a function */
exports.callMeMoby = function (x, theFunction) {
  let a = 0;
  for (a = 0; a < x; a++) {
    theFunction();
  }
};
