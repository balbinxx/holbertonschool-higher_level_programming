#!/usr/bin/node
const argx = parseInt(process.argv[2]);
if (!(Number.parseInt(argx))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argx; i++) {
    console.log('X'.repeat(argx));
  }
}
