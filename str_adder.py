def add(str):
    if str == "":
        return 0
    s = str.split(",")
    sf = []
    for string in s:
        sf.extend(string.split("\n"))
    sum = 0
    for val in sf:
        sum += int(val)

    return sum
