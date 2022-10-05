#!/usr/bin/node

function dummy (number, theFunction) {
  number = number + 1;
  theFunction(number);
}

exports.addMeMaybe = dummy;
