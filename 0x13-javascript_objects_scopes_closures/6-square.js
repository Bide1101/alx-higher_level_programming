#!/usr/bin/node
/* a class Square that defines a square and inherits from Square of 5-square.js */

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c) {
      for (let a = 0; a < this.height; a++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
