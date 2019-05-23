#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}
const li = process.argv;
let max = li[2];
let low = li[3];
for (let i = 3; i < process.argv.length; i += 1) {
  if (Number(li[i]) === Number(max)) {
    li.splice(i);
  }
  if (Number(li[i]) > Number(max)) {
    low = max;
    max = li[i];
  }
  if (i == process.argv.length) {
    if (low < li[i] < max) { 
      low = li[i];
    }
  }
}
console.log(low);
