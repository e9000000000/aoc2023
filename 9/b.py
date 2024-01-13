def count(line: list[int]) -> list[int]:
    return [line[i] - line[i - 1] for i in range(1, len(line))]

def prev_value(line: list[int]) -> int:
    line_set = set(line)
    if len(line_set) <= 1:
        return sum(line_set)

    return line[0] - prev_value(count(line))


with open('inp', 'r') as f:
    lines = list(map(lambda x: list(map(int, x.split())), f.read().splitlines()))


print(sum(map(prev_value, lines)))
