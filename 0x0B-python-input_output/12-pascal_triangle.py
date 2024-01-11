#!/usr/bin/python3
"""module taht defines the list"""


def pascal_triangle(n):
    """defines the triangle"""
    if n <= 0:
        return []
    a = []
    for b in range(n):
        row = [1] * (b + 1)
        for c in range(1, b):
            row[c] = a[b - 1][c - 1] + a[b - 1][c]
        a.append(row)
    return a
