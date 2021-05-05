#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const argv = process.argv;

request(url + argv[2], function (err, response, body) {
  if (err) { console.error('error:', err); }
  const results = JSON.parse(body);
  for (const char in results.characters) {
    request(results.characters[char], function (error, response, body) {
      if (error) { console.error('error:', error); }

      const b = JSON.parse(body);

      console.log(b.name);
    });
  }
});
