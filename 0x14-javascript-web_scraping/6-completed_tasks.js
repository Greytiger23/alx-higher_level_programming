#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Status code ' + response.statusCode);
  }

  const todos = JSON.parse(body);
  const c = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!c[todo.userId]) {
        c[todo.userId] = 1;
      } else {
        c[todo.userId]++;
      }
    }
  });
  console.log(c);
});
