import re

def add(s):
    delim = [",","\n"]
    if s[0:2] == "//":
        newline = s.index("\n")

        leftbracket = s[2:].find("[")
        rightbracket = s[2:newline][::-1].find("]")

        if leftbracket == -1 or rightbracket == -1:
            delim.append(s[2])
            s = s[4:]
        else:
            leftbracket += 2
            rightbracket = newline - 1 - rightbracket
            delim.append(s[leftbracket + 1: rightbracket])
            s = s[rightbracket + 1:]

        adj_delim = ""
        for character in delim[2]:
            if character == "[":
                adj_delim = adj_delim + "\\["
            else:
                 adj_delim = adj_delim + character

        delim[2] = adj_delim

    if s == "":
        return 0
    delim = "|".join(delim)
    s = list(filter(None, re.split(delim, s)))

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
