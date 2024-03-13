#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c = 'X') {
    let a = '';
    for (let b = 0; b < this.width; b++) {
      a += c;
    }
    for (let b = 0; b < this.height; b++) {
      console.log(a);
    }
  }
}
module.exports = Square;
