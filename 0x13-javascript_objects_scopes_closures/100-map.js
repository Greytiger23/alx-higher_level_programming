#!/usr/bin/node
const { list } = require('./100-data');
const a = list.map((value, index) => value * index);
console.log(list);
console.log(a);
