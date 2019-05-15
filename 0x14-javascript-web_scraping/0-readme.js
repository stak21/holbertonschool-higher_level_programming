#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
