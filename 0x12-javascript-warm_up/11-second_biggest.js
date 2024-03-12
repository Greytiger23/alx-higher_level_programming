#!/usr/bin/node
const x = process.argv.slice(2).map(Number);
if (x.length <= 1)
{
console.log(0);
}
else
{
const y = x.sort((a, b) => b - a);
console.log(y[1]);
}
