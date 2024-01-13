def count(line: list[int]) -> list[int]:
    return [line[i] - line[i - 1] for i in range(1, len(line))]

def next_value(line: list[int]) -> int:
    line_set = set(line)
    if len(line_set) <= 1:
        return sum(line_set)

    return line[-1] + next_value(count(line))


with open('inp', 'r') as f:
    lines = list(map(lambda x: list(map(int, x.split())), f.read().splitlines()))


print(sum(map(next_value, lines)))
