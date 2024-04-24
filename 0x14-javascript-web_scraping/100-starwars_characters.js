#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

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
  
  function fetchCharacterName(url) {
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

  Promise.all(c.map(url => fetchCharacterName(url)))
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});
