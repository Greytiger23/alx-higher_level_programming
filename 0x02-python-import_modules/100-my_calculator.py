#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
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
