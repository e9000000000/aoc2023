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

    def strait_range(self, dist_range):
        dist_start = dist_range.src_start
        src_start = max(dist_range.src_start - self.diff, self.src_start)
        stop = min((dist_range.src_stop - self.diff, self.dist_stop, self.src_stop))
        length = stop - src_start
        if length < 0:
            length = 0
        return Range(dist_start, src_start, length)

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


def ranges_to_get_here(dist_range: Range, c: Converter) -> list[Range]:
    result = []

    start_range = Range(dist_range.src_start, dist_range.src_start, c.ranges[0].src_start - dist_range.src_start)
    if not start_range.is_empty():
        result.append(start_range)

    for r in c.ranges:
        sr = r.strait_range(dist_range)
        if sr.is_empty():
            continue

        result.append(sr)

    end_range = Range(c.ranges[-1].src_stop, c.ranges[-1].src_stop, dist_range.src_stop - c.ranges[-1].src_stop)
    if not end_range.is_empty():
        result.append(end_range)

    return result


with open('tinp', 'r') as f:
    allblocks = f.read().split('\n\n')

seeds_block = allblocks[0]
blocks = allblocks[1:]

seed_ranges = []
raw_seed_ranges = list(map(int, seeds_block.split()[1:]))
for i in range(0, len(raw_seed_ranges), 2):
    range_start = raw_seed_ranges[i]
    length = raw_seed_ranges[i + 1]
    seed_ranges.append(Range(range_start, range_start, range_start + length))


converters = [Converter(block) for block in blocks]

# strait_ranges = converters[-1].ranges
# start_range = Range(0, 0, strait_ranges[0].src_start)
# if start_range:
#     strait_ranges = [start_range] + strait_ranges
strait_ranges = [Range(0, 0, 999999999999999999999)]

for c in reversed(converters):
    new_ranges = []
    for sr in strait_ranges:
        rtgh = ranges_to_get_here(sr, c)
        new_ranges += rtgh

    new_ranges = list(set(new_ranges))
    print(f"ranges to get from {c.ranges} to the end:\n{new_ranges}")
    strait_ranges = new_ranges


strait_ranges.sort(key=lambda r: r.dist_start)
print(strait_ranges)

x = 82
for sr in strait_ranges:
    if x in sr:
        print(f"counted X: {sr.dist_number(x)}")
for c in converters:
    x = c.convert(x)
print(f"TRUE X: {x}")

# for sr in strait_ranges:
#     for seed_range in seed_ranges:
#         sr_to_seed = seed_range.strait_range(sr)
#         print(sr_to_seed)






# lowest_location = 9999999999999999999999999999999999999999
# for seed_range in seed_ranges:
#     for seed in range(*seed_range):
#         number = seed
#         for c in converters:
#             number = c.convert(number)
#         lowest_location = min(lowest_location, number)

# print(f"lowest location is {lowest_location}")



# 0-10 -> 5-15 => 1-11 -> 7-17 => 2-12 -> 8-18

'''
we wanna get 8-18 so we wanna insert 2-12 into last one
we wanna get 2-12 from middel, so we should insert ...
we can get 7-12 from middle, we can't get 2, becouse 2 becomes 8 in middle one
so we sould insert ... to get 2-12
12 - 7 = 5 is a max value, 6 becomes 12, so it's bigger them our range
so `stop` of insert range will be 6
0 is too smol, it can't get into 1-11 range, so min value is 1
1-6 is our range



if 0-10 -> 1-11 => 3-5
2-4
if 0-10 -> 5-15 => 3-9
0-4





'''
