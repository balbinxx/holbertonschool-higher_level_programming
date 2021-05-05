#!/usr/bin/node

const request = require('request');

const argv = process.argv;

request(argv[2], function (err, response, body) {
  if (err) { console.error('error:', err); }
  const jsonbody = JSON.parse(body);

  const dic = {};
  for (const idx in jsonbody) {
    if (jsonbody[idx].completed === true) {
      if (dic[jsonbody[idx].userId] === undefined) {
        dic[jsonbody[idx].userId] = 0;
      }
      dic[jsonbody[idx].userId] += 1;
    }
  }

  console.log(dic);
});
