#!/usr/bin/node
const dict = require('./101-data').dict;
const new = Object.keys(dict).reduce(
  (acc, k) => (acc[dict[k]] = [...(acc[dict[k]] || []), k], acc), {});
console.log(new);
