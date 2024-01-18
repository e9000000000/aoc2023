with open('inp', 'r') as f:
    lines = f.read().splitlines()


galaxies = []

for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        if symbol == '#':
            galaxies.append([x, y])

for y in range(len(lines) - 1, -1, -1):
    is_there_any_galaxies = False
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            is_there_any_galaxies = True
    if not is_there_any_galaxies:
        for galaxy in galaxies:
            if galaxy[1] > y:
                galaxy[1] += 1

for x in range(len(lines[0]) - 1, -1, -1):
    is_there_any_galaxies = False
    for y in range(len(lines)):
        if lines[y][x] == '#':
            is_there_any_galaxies = True
    if not is_there_any_galaxies:
        for galaxy in galaxies:
            if galaxy[0] > x:
                galaxy[0] += 1



s = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        s += abs(galaxies[i][0] - galaxies[j][0])
        s += abs(galaxies[i][1] - galaxies[j][1])

print(s)
