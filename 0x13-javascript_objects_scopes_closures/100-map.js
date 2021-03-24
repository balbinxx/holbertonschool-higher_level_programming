#!/usr/bin/node
const data = require('./100-data').list;
const new = data.map((x, i) => i * x);
console.log(data);
console.log(new);
