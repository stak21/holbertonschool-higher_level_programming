#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
  process.exit();
}
const li = process.argv;
let max = li[2];
let low = max;
for (let i = 3; i < process.argv.length; i += 1) {
  if (Number(li[i]) > Number(max)) {
    low = max;
    max = li[i];
  }
}
console.log(low);
