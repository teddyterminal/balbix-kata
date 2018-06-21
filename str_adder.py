def add(str):
    if str == "":
        return 0
    s = str.split(",")
    sum = 0
    for val in s:
        sum += int(val)

    return sum
