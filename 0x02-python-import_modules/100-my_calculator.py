#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
d = argv[2]
b = int(argv[3])
x = 0
if d == '+':
    x = add(a, b)
elif d == '-':
    x = sub(a, b)
elif d == '*':
    x = mul(a, b)
elif d == '/':
    x = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
print("{:d} {:s} {:d} = {:d}".format(a, d, b, x))
exit(0)
