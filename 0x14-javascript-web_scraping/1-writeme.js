#!/usr/bin/node

if (process.argv.length >= 3) {
  const fs = require('fs');
  let path = process.argv[2];
  let s = process.argv[3];

  fs.writeFile(path, s, (err) => {
    if (err) { console.log(err); }
  });
}
