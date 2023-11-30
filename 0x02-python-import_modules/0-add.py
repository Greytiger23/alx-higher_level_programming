#!/usr/bin/python3
a = 1
b = 2
add_0 = __import__('add_0', fromlist=['add'])
sum = add_0.add(a, b)
print("{} + {} = {}".format(a, b, sum))
