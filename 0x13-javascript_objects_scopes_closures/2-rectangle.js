#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w=null, h=null) {
    if (h <= 0 || w <= 0) {
      return null;
    }
    else {
    this.width = w;
    this.height = h;
  }
  }
};
