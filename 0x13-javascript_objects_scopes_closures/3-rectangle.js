#!/usr/bin/node
/* This class defines a Rectangle with a constructor and creates an instance method */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let wid = 0; wid < this.height; wid++) {
      let r = '';
      for (let heg = 0; heg < this.width; heg++) {
        r += 'X';
      }
      console.log(r);
    }
  }
};
