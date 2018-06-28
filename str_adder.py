import re

def add(str):
    delim = [",","\n"]
    if str[0:2] == "//":
        delim.append(str[2])
        str = str[4:]

    sf = []
    if str == "":
        return 0
    delim = "|".join(delim)
    s = re.split(delim, str)

    sum = 0
    for val in s:
        if int(val) < 0:
            raise Exception("negatives not allowed")
        sum += int(val)

    return sum
