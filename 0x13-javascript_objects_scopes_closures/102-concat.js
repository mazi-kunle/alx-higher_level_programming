#!/usr/bin/node

const argv = process.argv;
const filea = argv[2];
const fileb = argv[3];
const filec = argv[4];

const fs = require('fs');
fs.readFile(filea, 'utf8', function (err, data) {
  fs.writeFile(filec, data, function(err) {
    if (err) { throw err; }
  });
});

fs.readFile(fileb, 'utf8', function (err, data) {
  fs.appendFile(filec, data, function(err) {
    if (err) { throw err; }
  });
});
