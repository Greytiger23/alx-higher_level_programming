#!/usr/bin/node
exports.esrever = function (list) {
  const a = [];
  for (let b = list.length - 1; b >= 0; b--) {
    a.push(list[b]);
  }
  return a;
};
