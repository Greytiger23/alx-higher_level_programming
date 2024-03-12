#!/usr/bin/node
const a = process.argv[2];
if (!isNaN(a)) {
  console.log('My number:', parseInt(a));
} else {
  console.log('Not a number');
}
