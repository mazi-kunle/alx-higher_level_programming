#!/usr/bin/node

const arr = require('./100-data.js').list;
const arr2 = arr.map(function (element, index) { return (index * element); });
console.log(arr);
console.log(arr2);
