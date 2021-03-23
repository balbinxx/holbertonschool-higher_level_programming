#!/usr/bin/node
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const n = process.argv[2];
const facto = factorial(n);
console.log(facto);
