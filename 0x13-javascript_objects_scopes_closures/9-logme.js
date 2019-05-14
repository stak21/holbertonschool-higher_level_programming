#!/usr/bin/node
let total = 0;

exports.logMe = item => {
  console.log(total + ': ' + item);
  total += 1;
};
