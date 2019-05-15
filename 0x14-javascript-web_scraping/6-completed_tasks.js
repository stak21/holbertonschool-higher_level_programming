#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let users = {};
request.get(url, function (body, err, response) {
  let tasks = JSON.parse(response);
  tasks.forEach(task => {
    if (users[task['userId']] === undefined) {
      users[task['userId']] = 0;
    }
    if (task['completed'] === true) {
      users[task['userId']] += 1;
    }
  });
  console.log(users);
});
