from functools import reduce

def moves_gen(instrs):
    while 1:
        for i in instrs:
            yield i


def make_nodes(lines: list[str]) -> dict:
    nodes = {}
    for line in lines:
        nodes[line[:3]] = (line[7:10], line[12:15])
    return nodes


def split_for_primes(number: int) -> list[int]:
    primes = []
    x = 2
    while number > 1:
        if number % x == 0:
            number //= x
            primes.append(x)
        else:
            x += 1
    return primes


with open('inp', 'r') as f:
    instruction, raw_lines = f.read().split('\n\n')
    lines = raw_lines.splitlines()

instrs = tuple(map(lambda x: 1 if x == "R" else 0, instruction))
nodes = make_nodes(lines)

current_alpha = [node for node in nodes if node.endswith('A')]
longs = {}
for c in current_alpha:
    counter = 0
    moves = moves_gen(instrs)
    while not c.endswith('Z'):
        counter += 1
        c = nodes[c][next(moves)]

    longs[c] = counter

print(longs)

lprimes = list(map(split_for_primes, longs.values()))
primeset = set()
for chunk in lprimes:
    for prime in chunk:
        primeset.add(prime)
print(primeset)
print(reduce(lambda s, x: s * x, primeset))
