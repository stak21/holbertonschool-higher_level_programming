#!/usr/bin/node

let fs = require('fs');

if (!process.argv[2]) { process.exit(); }
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
