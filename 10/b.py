import sys
from enum import Enum
from dataclasses import dataclass


class PathType(Enum):
    PATH = -1
    NOT_PATH = -2
    UNDISCOVERED = -3
    START = -4

Pipes = list[list[str]]
PathMap = list[list[int]]


@dataclass
class Point:
    x: int
    y: int


CONNECTS = {
    '|': (Point(0, 1), Point(0, -1)),
    '-': (Point(1, 0), Point(-1, 0)),
    'L': (Point(0, -1), Point(1, 0)),
    'J': (Point(0, -1), Point(-1, 0)),
    '7': (Point(0, 1), Point(-1, 0)),
    'F': (Point(0, 1), Point(1, 0)),
    '.': (),
    'S': (Point(0, 1), Point(0, -1), Point(1, 0), Point(1, -1)),
}


def new_path_map(pipes: Pipes):
    return [[0 for _ in pipes[y]] for y in range(len(pipes))]


def print_path_map(path_map: PathMap):
    for row in path_map:
        for s in row:
            if s == PathType.PATH:
                print('p', end='')
            elif s == PathType.START:
                print('S', end='')
            elif s == PathType.UNDISCOVERED:
                print('X', end='')
            elif s == PathType.NOT_PATH:
                print('.', end='')
            else:
                print(' ', end='')
        print()


def locate_starting_point(pipes: Pipes) -> Point:
    for y in range(len(pipes)):
        for x, pipe in enumerate(pipes[y]):
            if pipe == 'S':
                return Point(x, y)
    raise ValueError('no S in pipes')


def is_legit_point(path_map: PathMap, p: Point) -> bool:
    return p.x >= 0 and p.y >= 0 and p.y < len(path_map) and p.y < len(path_map[p.y]) and path_map[p.y][p.x] in (0, PathType.START)


def next_awailable_points(pipes: Pipes, path_map: PathMap, point: Point) -> list[Point]:
    awailable_point = CONNECTS[pipes[point.y][point.x]]
    points = tuple(map(lambda p: Point(point.x + p.x, point.y + p.y), awailable_point))
    return [p for p in points if is_legit_point(path_map, p)]


def mark_as_not_path(path_map: PathMap, p: Point):
    path_map[p.y][p.x] = PathType.NOT_PATH


def mark_as_path(path_map: PathMap, p: Point):
    path_map[p.y][p.x] = PathType.PATH


def mark_as_undiscovered(path_map: PathMap, p: Point):
    path_map[p.y][p.x] = PathType.UNDISCOVERED


def mark_as_start(path_map: PathMap, p: Point):
    path_map[p.y][p.x] = PathType.START


def build_path_map(pipes: Pipes, path_map: PathMap, point: Point, *, count=0, first_call=False) -> int:
    if pipes[point.y][point.x] == 'S':
        mark_as_start(path_map, point)
        if not first_call:
            return count
    else:
        mark_as_undiscovered(path_map, point)
    next_points = next_awailable_points(pipes, path_map, point)
    if len(next_points) == 0:
        mark_as_not_path(path_map, point)
        return -1

    for point in next_points:
        next_count = build_path_map(pipes, path_map, point, count=count)
        if next_count >= 0:
            mark_as_path(path_map, point)
            return next_count + 1
        else:
            mark_as_not_path(path_map, point)
            return -1

with open('tinp3', 'r') as f:
    pipes = f.read().splitlines()
    sys.setrecursionlimit(len(pipes) * len(pipes[0]))

path_map = new_path_map(pipes)
print(build_path_map(pipes, path_map, locate_starting_point(pipes), first_call=True) / 2)
print_path_map(path_map)


