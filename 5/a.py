class Range:
    """*_stop is not included"""

    def __init__(self, dist_start: int, src_start: int, length: int):
        self.src_start = src_start
        self.src_stop = src_start + length
        self.dist_start = dist_start
        self.dist_stop = dist_start + length

    def __contains__(self, src_number: int) -> bool:
        return src_number >= self.src_start and src_number < self.src_stop

    def __repr__(self):
        return f"{self.src_start}-{self.src_stop} {self.dist_start}-{self.dist_stop}"

    def dist_number(self, src_number: int) -> int:
        """use ONLY if this range contains src_number"""

        return self.dist_start + (src_number - self.src_start)


class Converter:
    def __init__(self, block: str):
        lines = block.splitlines()
        what_to_what = lines[0].split()[0].split('-')
        raw_ranges = lines[1:]

        self.src = what_to_what[0]
        self.dist = what_to_what[2]
        self.ranges = [Range(*map(int, rr.split())) for rr in raw_ranges]


    def convert(self, src_number: int) -> int:
        for r in self.ranges:
            if src_number in r:
                return r.dist_number(src_number)
        return src_number


with open('tinp', 'r') as f:
    allblocks = f.read().split('\n\n')

seeds_block = allblocks[0]
blocks = allblocks[1:]

seeds = list(map(int, seeds_block.split()[1:]))
converters = [Converter(block) for block in blocks]

locations = []
for seed in seeds:
    number = seed
    for c in converters:
        number = c.convert(number)
    locations.append(number)
    print(f"{seed} -> {number}")

print(f"lowest location is {min(locations)}")
