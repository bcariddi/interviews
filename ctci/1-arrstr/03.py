#!/usr/bin/env python3

def URLify(s):
    return s.replace(' ', '%20')

def main():
    s = 'kevin de bruyne'
    s = URLify(s)
    print(s)

if __name__ == '__main__':
    main()
