#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let first = -Infinity;
  let second = -Infinity;
  const arr = process.argv;
  for (let i = 2; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }
  console.log(second);
}
