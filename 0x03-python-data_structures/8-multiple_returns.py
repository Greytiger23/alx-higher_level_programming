#!/usr/bin/python3
def multiple_returns(sentence):
    b = len(sentence)
    a = sentence[0] if b > 0 else None
    return b, a
