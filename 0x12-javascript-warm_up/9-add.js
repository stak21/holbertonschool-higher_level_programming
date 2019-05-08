#!/usr/bin/node
function add (a, b) {
  a = parseInt(a, 10);
  b = parseInt(b, 10);
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  }
  return (a + b);
}

const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
