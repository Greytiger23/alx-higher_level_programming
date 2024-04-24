#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const p = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Status code ' + response.statusCode);
  }

  fs.writeFile(p, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
