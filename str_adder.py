import re

def add(s):
    delim = [",","\n"]
    if s[0:2] == "//":
        if s[2] != "[":
            delim.append(s[2])
            s = s[4:]
        else:
            delim.append(s[3:s.index("]")])
            s = s[s.index("]")+1:]

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
