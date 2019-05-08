#!/usr/bin/node
function fac (num) {
  num = parseInt(num, 10);
  if (num === 1 || isNaN(num)) { return (1); }
  return (fac(num - 1) * num);
}

console.log(fac(process.argv[2]));
