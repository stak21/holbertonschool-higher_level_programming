#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
  charPrint (c) {
    if (c === null || c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i += 1) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
