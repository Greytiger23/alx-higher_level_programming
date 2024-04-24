#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Status code ' + response.statusCode);
  }

  const m = JSON.parse(body);
  const c = m.characters;
 
  function fetchCharacterName (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          console.error('Error: Status code ' + response.statusCode);
        }
        const a = JSON.parse(body);
        resolve(a.name);
      });
    });
  }

  c.reduce((promiseChain, url) => {
    return promiseChain.then(() => {
      return fetchCharacterName(url).then(name => {
        console.log(name);
      });
    });
  }, Promise.resolve())
    .catch(error => {
      console.error(error);
    });
});
