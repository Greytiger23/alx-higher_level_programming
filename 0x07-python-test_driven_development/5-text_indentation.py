#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in text:
        if a == '.' or a == '?' or a == ':':
            print("\n")
        else:
            print(a, end='')
