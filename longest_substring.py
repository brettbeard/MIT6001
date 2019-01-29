#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_substring(s):

    previous_ascii = 0
    substring = ''
    temp_substring = ''

    # iterate through each character in string
    for ch in s:

        # convert char to ASCII value
        ascii = ord(ch)

        # check if in alphabetical order
        if ascii >= previous_ascii:
            temp_substring += ch

            # is this the longest substring?
            if len(temp_substring) > len(substring):
                substring = temp_substring
        else:
            # clear out substring
            temp_substring = ch

        # update previous ascii value
        previous_ascii = ascii

    return substring


def main():
    """ Main program """
    test_values = ["abcdefghijklmnopqrstuvwxyz", "azcbobobegghakl", "abcbcd"]

    for item in test_values:
        print (item)
        result = find_substring(item)
        print ("Longest substring in alphabetical order is: " + result)

    return 0


if __name__ == "__main__":
    main()
