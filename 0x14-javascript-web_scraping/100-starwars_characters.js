#!/usr/bin/node

const request = require('request');
if (process.argv.length >= 3) {
  let url = 'http://swapi.co/api/films/' + process.argv[2];
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let characters = JSON.parse(body)['characters'];
      characters.forEach(url => {
        request(url, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body)['name']);
          }
        });
      });
    }
  });
}
