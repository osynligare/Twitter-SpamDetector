#!/usr/bin/env python

def heuristic(string, size):
    # Initialize all occurence as -1 in ASCII char array
    bad_char = [-1] * 256
 
    # Fill the actual value of last occurence
    for i in range(size):
        bad_char[ord(string[i])] = i;

    # retun initialized list
    return bad_char

def BoyerMoore(big_string, pattern):
    len_s = len(big_string)
    len_p = len(pattern)

    bad_char = heuristic(pattern, len_p)

    shift = 0
    while(shift <= len_s - len_p):
        j = len_p - 1

        while j >= 0 and pattern[j] == big_string[shift + j]:
            j -= 1
 
        if j < 0:
            print("Pattern occur at character {}.".format(shift))
            return shift
        else:
            shift += max(1, j - bad_char[ord(big_string[shift + j])])


# Driver program to test above funtion
def main():
    big_string = raw_input("Input string:")
    small_string = raw_input("Input pattern:")
    BoyerMoore(big_string, small_string)

if __name__ == '__main__':
    main()