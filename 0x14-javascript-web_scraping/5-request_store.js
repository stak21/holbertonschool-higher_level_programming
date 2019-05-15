#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2]).on('error', function (err) {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
