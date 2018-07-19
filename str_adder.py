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

        flag = True
        s2 = s[2:]
        while flag == True:
            #determine whether the delimiter string (from 2 onwards) has a bracket
            leftbracket = s2.find("[")
            rightbracket = s2.find("]")

            if leftbracket == -1:
                flag = False
                continue

            delim.append(s2[leftbracket + 1: rightbracket])
            s2 = s2[rightbracket + 1:]


        #still might have single delimiter
        newline = s2.find("\n")
        if newline != 0:
            delim.append(s2[0:newline])

        s = s2

        #code to clear regex
        for i in range(2, len(delim)):
            adj_delim = ""
            for character in delim[i]:
                if character in ["[", "]", "*", "+", "?", "^"]:
                    adj_delim = adj_delim + "\\" + character
                else:
                    adj_delim = adj_delim + character

            delim[i] = adj_delim

    return delim, s
