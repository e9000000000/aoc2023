def move_generator(instructions: str):
    instrs = tuple(map(lambda x: 1 if x == "R" else 0, instructions))
    step = 1
    while 1:
        for instr in instrs:
            yield instr, step
            step += 1


def make_nodes(lines: list[str]) -> dict:
    nodes = {}
    for line in lines:
        nodes[line[:3]] = (line[7:10], line[12:15])
    return nodes


with open('inp', 'r') as f:
    instruction, raw_lines = f.read().split('\n\n')
    lines = raw_lines.splitlines()

moves = move_generator(instruction)
nodes = make_nodes(lines)

current = 'AAA'
while current != 'ZZZ':
    move = next(moves)
    current = nodes[current][move[0]]
    print(current, move)


