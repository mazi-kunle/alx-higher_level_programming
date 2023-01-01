#!/usr/bin/node
const argv = process.argv;

let num = argv[2];

if (!num) {
  console.log('Not a number');
} else {
  num = parseInt(num, 10);
  if (!num) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
}
