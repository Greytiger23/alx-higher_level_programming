#!/usr/bin/node
const a = process.argv[2];
const x = parseInt(a);
if (!isNaN(x)) {
  for (let b = 0; b < x; b++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
