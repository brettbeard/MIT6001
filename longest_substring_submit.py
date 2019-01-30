def find_substring2(s):

    temp_substring = ''
    longest_substring = ''
    previous_char = ''

    # iterate through each character in string
    for ch in s:
        if ch >= previous_char:
            # append the character
            temp_substring += ch

            # is this the longest sub-string?
            if len(temp_substring) > len(longest_substring):
                # update the longest sub-string
                longest_substring = temp_substring
        else:
            temp_substring = ch

        # save off the previous character
        previous_char = ch

    return longest_substring

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

#s = 'lsfdxppvnepjibzlm'
s = 'azcbobobegghakl'
result = find_substring2(s)
print ("Longest substring in alphabetical order is: " + result)