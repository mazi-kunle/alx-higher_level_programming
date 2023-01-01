#!/usr/bin/node

const str = 'C is fun';
const argv = process.argv;

if (!argv[2] || !parseInt(argv[2], 10)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(argv[2], 10);

  for (let i = 0; i < num; i++) {
    console.log(str);
  }
}
