#!/usr/bin/node
function factorial(n) {
    if (!n) {
        return 1; 
    } else {
        return n * factorial(n-1);
    }
}
let n = process.argv[2];
let facto = factorial(n)
console.log(facto);
