#!/usr/bin/node
const a = require('fs');
const b = a.readFileSync(process.argv[2]).toString();
const c = a.readFileSync(process.argv[3]).toString();
a.writeFileSync(process.argv[4], b + c);
