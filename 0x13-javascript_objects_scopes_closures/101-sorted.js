#!/usr/bin/node
const { dict } = require('./101-data');
const a = {};
for (const [userId, occurrences] of Object.entries(dict)) {
  if (occurrences in a) {
    a[occurrences].push[userId];
  } else {
    a[occurrences] = [userId];
  }
}
console.log(a);
