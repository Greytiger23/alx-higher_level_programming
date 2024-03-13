#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      return;
    }
    for (let a = 0; a < this.height; a++) {
      let c = '';
      for (let b = 0; b < this.width; b++) {
        c += 'X';
      }
      console.log(c);
    }
  }
}
module.exports = Rectangle;
