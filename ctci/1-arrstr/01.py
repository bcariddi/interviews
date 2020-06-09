#!/usr/bin/env python3

def has_unique(s):
    chars = {}

    for char in s:
        if char in chars:
            return False
        else:
            chars[char] = 1

    return True

def main():
    strings = ['abcdefghijklmnopqrstuvwxyz', 'briancariddi', ' ', 'hey man']
    for string in strings:
        if has_unique(string):
            output = string + ' is unique!'
        else:
            output = string + ' is not unique'
        print(output)

if __name__ == '__main__':
    main()
