#!/usr/bin/node

const request = require('request');

let users = {};
if (process.argv.length >= 3) {
  const url = process.argv[2];
  request.get(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      try {
        let tasks = JSON.parse(body);
        tasks.forEach(task => {
          if (task['completed'] === true) {
            if (users[task['userId']] === undefined) {
              users[task['userId']] = 0;
            }
            users[task['userId']] += 1;
          }
        });
        console.log(users);
      } catch(error) {
        throw error
      }
    }
  });
}
