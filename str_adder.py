import re

def add(s):

    #process delimiter and get only add string
    delim, s = process_delimiter(s)

    #split string into integer additions
    if s == "":
        return 0
    delim = "|".join(delim)
    s = list(filter(None, re.split(delim, s)))

    #add and disallow negatives
    sum = 0
    negatives = []
    for val in s:
        if int(val) < 0:
            negatives.append(str(int(val)))

        if (int(val) <= 1000):
            sum += int(val)

    if (len(negatives) > 0):
        raise Exception("negatives not allowed: (" + ", ".join(negatives) + ")")

    return sum

def process_delimiter(s):

    #base case: delimiter is comma or newline
    delim = [",","\n"]

    if s[0:2] == "//":            #we have a custom delimiter
        newline = s.index("\n")

        #determine whether the delimiter string (from 2 onwards) has a bracket
        leftbracket = s[2:].find("[")
        rightbracket = s[2:newline][::-1].find("]")

        if leftbracket == -1 or rightbracket == -1: #this is a single custom delimiter
            delim.append(s[2])
            s = s[4:]
        else: #This is a multiple character delimiter
            leftbracket += 2                                #index of the left bracket of the multi-char delimiter
            rightbracket = newline - 1 - rightbracket       #index of the right bracket of the multi-char delimiter
            delim.append(s[leftbracket + 1: rightbracket])
            s = s[rightbracket + 1:]

        #code to get characters in the custom delimiter that are left brackets for regex
        adj_delim = ""
        for character in delim[2]:
            if character == "[":
                adj_delim = adj_delim + "\\["
            else:
                 adj_delim = adj_delim + character

        delim[2] = adj_delim

    return delim, s
