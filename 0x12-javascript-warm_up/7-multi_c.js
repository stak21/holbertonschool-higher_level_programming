#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
}
const x = parseInt(process.argv[2], 10);
for (let i = 0; i < x; i += 1) {
  console.log('C is fun');
}
