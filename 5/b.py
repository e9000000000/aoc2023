class Range:
    """*_stop is not included"""

    def __init__(self, dist_start: int, src_start: int, length: int):
        self.src_start = src_start
        self.src_stop = src_start + length
        self.dist_start = dist_start
        self.dist_stop = dist_start + length
        self.diff = self.dist_start - self.src_start

    def __contains__(self, src_number: int) -> bool:
        return src_number >= self.src_start and src_number < self.src_stop

    def __repr__(self):
        if self.is_empty():
            return "X"

        return f"{self.src_start}-{self.src_stop} {self.dist_start}-{self.dist_stop}"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return repr(self) == repr(other)

    def dist_number(self, src_number: int) -> int:
        """use ONLY if this range contains src_number"""

        return src_number + self.diff

    def is_empty(self) -> bool:
        return self.src_start >= self.src_stop


class Converter:
    def __init__(self, block: str):
        lines = block.splitlines()
        self.what_to_what = lines[0].split()[0].split('-')
        raw_ranges = lines[1:]

        self.src = self.what_to_what[0]
        self.dist = self.what_to_what[2]
        self.ranges = [Range(*map(int, rr.split())) for rr in raw_ranges]
        self.ranges.sort(key=lambda r: r.src_start)


    def convert(self, src_number: int) -> int:
        for r in self.ranges:
            if src_number in r:
                return r.dist_number(src_number)
        return src_number


def create_range(src_start: int, src_stop: int, diff: int) -> Range:
    return Range(src_start + diff, src_start, src_stop - src_start)


def skiping_ranges(r: Range, c: Converter) -> list[Range]:
    result = []
    start_range = create_range(r.src_start, c.ranges[0].src_start - r.diff, r.diff)
    if not start_range.is_empty():
        result.append(start_range)

    for cr in c.ranges:
        mid_range = create_range(max(r.src_start, cr.src_start - r.diff), min(r.src_stop, cr.src_stop - r.diff), r.diff + cr.diff)
        if not mid_range.is_empty():
            result.append(mid_range)

    end_range = create_range(max(c.ranges[-1].src_stop - r.diff, r.src_start), r.src_stop, r.diff)
    if not end_range.is_empty():
        result.append(end_range)
    return result


with open('inp', 'r') as f:
    allblocks = f.read().split('\n\n')

seeds_block = allblocks[0]
blocks = allblocks[1:]

seed_ranges = []
raw_seed_ranges = list(map(int, seeds_block.split()[1:]))
for i in range(0, len(raw_seed_ranges), 2):
    range_start = raw_seed_ranges[i]
    length = raw_seed_ranges[i + 1]
    seed_ranges.append(create_range(range_start, range_start + length, 0))


converters = [Converter(block) for block in blocks]


rs = seed_ranges
for c in converters:
    new_rs = []
    for r in rs:
        new_rs += skiping_ranges(r, c)
    rs = new_rs

lowest = 9999999999999999999999999999999
for r in rs:
    lowest = min(lowest, r.dist_start)

print(lowest)
