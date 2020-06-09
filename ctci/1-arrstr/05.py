#!/usr/bin/env python3

def length_conditions(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    return True

def is_one_away(s1, s2):
    # same string
    if s1 == s2:
        return True

    # same length - must be a 'replace'
    if len(s1) == len(s2):
        onediff = False
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if not onediff:
                    onediff = True
                else:
                    return False
        if onediff:
            return True

    # different length - must be an 'insert' to the shorter string, which is the first parameter in this function
    else:
        edited = False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False
                edited = True
                j += 1
            else:
                i += 1
                j += 1
        return True


def main():
    s1 = 'uck'
    s2 = 'fuck'

    if not length_conditions(s1, s2):
        print('not one away')
        return

    # TODO: switch s1 and s2 so that s1 is shorter if there's a length difference
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if is_one_away(s1, s2):
        print('ONE AWAY')
    else:
        print('not one away')

if __name__ == '__main__':
    main()
