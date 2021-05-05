#!/usr/bin/node

const request = require('request');
const argv = process.argv;
let counter = 0;
request(argv[2], function (error, response, body) {
  if (err) { console.error('error:', err); }

  const results = JSON.parse(body).results;
  for (const x in results) {
    for (const char in results[x].characters) {
      if (results[x].characters[char].endsWith('/18/')) {
        counter++;
      }
    }
  }
  return console.log(counter);
});
