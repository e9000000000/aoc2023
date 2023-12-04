from pprint import pp


with open("tinput.txt", "r") as f:
    lines = f.read().splitlines()

nums = []

current_num = ""
for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if symbol.isdigit():
            current_num += symbol
            if x+1 == len(line) or not line[x+1].isdigit():
                nums.append({"num": int(current_num), "x": x - len(current_num) + 1, "y": y, "h": 1, "w": len(current_num)})
                current_num = ""

fail_nums = []
result = 0
for num in nums:
    is_adjacent = False
    for y in range(max(num["y"] - 1, 0), min(num["y"] + num["h"] + 1, len(lines))):
        for x in range(max(num["x"] - 1, 0), min(num["x"] + num["w"] + 1, len(lines))):
            symbol = lines[y][x]
            if not symbol.isdigit() and symbol != ".":
                is_adjacent = True
    if is_adjacent:
        result += num["num"]
    else:
        fail_nums.append(num)

print(result)
pp(fail_nums)
