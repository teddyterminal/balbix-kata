import re

def add(s):
    delim = [",","\n"]
    if s[0:2] == "//":
        delim.append(s[2])
        s = s[4:]

    if s == "":
        return 0
    delim = "|".join(delim)
    s = re.split(delim, s)

    sum = 0
    negatives = []
    for val in s:
        if int(val) < 0:
            negatives.append(str(int(val)))
        sum += int(val)

    if (len(negatives) > 0):
        raise Exception("negatives not allowed: (" + ", ".join(negatives) + ")")

    return sum
