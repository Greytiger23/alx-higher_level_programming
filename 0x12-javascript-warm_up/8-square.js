#!/usr/bin/node
const a = process.argv[2];
const b = parseInt(a);
if (!isNaN(b)) {
  for (let i = 0; i < b; i++) {
    let y = '';
    for (let j = 0; j < b; j++) {
      y += 'X';
    }
    console.log(y);
  }
} else {
  console.log('Missing size');
}
