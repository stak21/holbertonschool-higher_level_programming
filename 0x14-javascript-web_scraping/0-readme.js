#!/usr/bin/node

let fs = require("fs");

let path = './' + process.argv[2];
fs.readFile(path, 'utf8', function (err, data) {
  if (err){
    console.log(err)
  } else {
    console.log(data)
  }
});
