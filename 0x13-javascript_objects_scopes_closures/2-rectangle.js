#!/usr/bin/node
/* This defines a Rectangle with a constructor and check if w or h is <= 0 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
