#!/usr/bin/env python3

def check_next(s, i):
    return s[i] == s[i + 1]

def compress(s):
    newstr = ''
    compressed = False
    i = 0
    while i < len(s):
        count = 1
        char = s[i]
        while i < len(s) - 1 and check_next(s, i):
            if not compressed: compressed = True
            i += 1
            count += 1
        newstr += s[i] + str(count)
        i += 1

    if not compressed:
        return s
    return newstr


def main():
    s = 'aabcccccaaa'
    s1 = 'abcd'
    print(compress(s))

if __name__ == '__main__':
    main()
