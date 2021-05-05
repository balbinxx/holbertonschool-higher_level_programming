#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const argv = process.argv;

request(argv[2], function (err, response, body) {
  if (err) { console.error('error:', err); }

  fs.writeFileSync(argv[3], body, 'utf-8', { flag: 'a+' }, err => { return console.log(err); });
});
