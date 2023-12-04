from pprint import pp


with open("input.txt", "r") as f:
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

gear_nums = []
for num in nums:
    is_adjacent = False
    for y in range(max(num["y"] - 1, 0), min(num["y"] + num["h"] + 1, len(lines))):
        for x in range(max(num["x"] - 1, 0), min(num["x"] + num["w"] + 1, len(lines))):
            symbol = lines[y][x]
            if symbol == "*":
                is_adjacent = True
                num["gear"] = {"x": x, "y": y}
                gear_nums.append(num)


gears = {}
for num in gear_nums:
    gear_hash = str(num["gear"])
    if gear_hash not in gears:
        gears[gear_hash] = []
    gears[gear_hash].append(num["num"])


result = 0
for gear in gears.values():
    if len(gear) == 2:
        result += gear[1] * gear[0]

print(result)
pp(gears)
