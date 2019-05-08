#!/usr/bin/node
if (process.argv.length == 2) {
  console.log('Missing size');
  process.exit();
}
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
  process.exit();
}

for (let i = 0; i < size; i += 1) {
  console.log('X'.repeat(size));
}
