#!/usr/bin/env python3

def char_counts(s):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    return counts

def is_palindrome_perm(counts, even):
    if even:
        for count in counts.values():
            if count != 2:
                return False
        return True
    else:
        oneone = False
        for count in counts.values():
            if count == 1:
                if not oneone:
                    oneone = True
                else:
                    return False
            elif count != 2:
                return False

        if oneone:
            return True

def main():
    s = 'tact coa'  
    s = s.replace(' ', '')

    even = False
    if len(s) % 2 == 0:
        even = True

    counts = char_counts(s)
    
    if is_palindrome_perm(counts, even):
        print('IS PALINDROME PERMUTATION!')
    else:
        print('nah')


if __name__ == '__main__':
    main()
