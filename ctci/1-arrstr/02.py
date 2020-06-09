#!/usr/bin/env python3

def is_perm_one_dict(s1, s2):
    if len(s1) != len(s2):
        return False

    chars = {}

    for c1, c2 in zip(s1, s2):
        chars[c1] = chars.get(c1, 0) + 1
        chars[c2] = chars.get(c2, 0) - 1

    for count in chars.values():
        if count != 0:
            return False

    return True

def is_perm(s1, s2):
    if len(s1) != len(s2):
        return False

    chars1 = {}
    chars2 = {}

    for char1, char2 in zip(s1, s2):
        chars1[char1] = chars1.get(char1, 0) + 1
        chars2[char2] = chars2.get(char2, 0) + 1

    if chars1 == chars2:
        return True

    return False

def main():
    s1 = 'brian'
    s2 = 'nairb'

    if is_perm_one_dict(s1, s2):
        print('PERMUTATIONS')
    else:
        print('nah')


if __name__ == '__main__':
    main()
