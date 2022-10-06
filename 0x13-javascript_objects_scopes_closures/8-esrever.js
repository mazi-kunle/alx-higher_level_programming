#!/usr/bin/node

exports.esrever = function (list) {
  const nlist = [];
  while (list.length > 0) {
    nlist.push(list.pop());
  }
  return (nlist);
};
