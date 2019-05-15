#!/usr/bin/node

const request = require('request');
if (process.argv.length >= 3) {
  let url = process.argv[2];
  let sub = '18';
  let count = 0;

  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let listOfMovies = JSON.parse(body)['results'];
      listOfMovies.forEach(movie => {
        let characters = movie['characters'];
        characters.forEach(id => {
          if (id.includes(sub)) {
            count += 1;
          }
        });
      });
    }
    console.log(count);
  });
}
