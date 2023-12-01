import re


tb = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

with open("input.txt", "r") as f:
    text = f.read().splitlines()
    sm = 0
    for line in text:
        m = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9|0))", line)
        add = int(str(tb[m[0]]) + str(tb[m[-1]]))
        sm += add
    print(sm)

