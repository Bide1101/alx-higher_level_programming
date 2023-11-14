#!/usr/bin/node
/* This class defines a Rectangle with a constructor, creates instance attributes and methods */
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

  rotate () {
    let temp = 0;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
