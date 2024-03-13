#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  for (const b of list) {
    if (b === searchElement) {
      a++;
    }
  }
  return a;
};
