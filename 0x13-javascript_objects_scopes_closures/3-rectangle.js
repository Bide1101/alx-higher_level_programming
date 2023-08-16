#!/usr/bin/node
/* class Rectangle that defines a rectangle  */

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let width = 0; width < this.height; width++) {
      let row = '';
      for (let height = 0; height < this.width; height++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
