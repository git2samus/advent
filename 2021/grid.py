#!/usr/bin/env python3
from typing import Any, Generator
from collections import namedtuple


Coord = namedtuple("Coord", ["x", "y"])


class Grid:
    def __init__(self, width: int, height: int, fill: Any = None):
        self._storage = [
            [fill for _ in range(width)] for _ in range(height)
        ]
        self.width, self.height = width, height

    def __getitem__(self, coord: Coord) -> Any:
        return self._storage[coord.y][coord.x]

    def __setitem__(self, coord: Coord, value: Any):
        if not (0 <= coord.x < self.width and 0 <= coord.y < self.height):
            raise IndexError

        self._storage[coord.y][coord.x] = value

    def __contains__(self, value: Any) -> bool:
        return any(value in row for row in self._storage)

    def __len__(self) -> int:
        return self.width * self.height

    def __iter__(self) -> Generator[Any, None, None]:
        for row in self._storage:
            for cell in row:
                yield cell

    def __repr__(self) -> str:
        return self._storage.__repr__()

    def __str__(self) -> str:
        return self._storage.__str__()

    @classmethod
    def from_iterable(cls, iterable) -> "Grid":
        result = cls(0, 0)

        result._storage = [
            list(row) for row in iterable
        ]
        result.height = len(result._storage)
        result.width = len(result._storage[0])

        return result

    @property
    def rows(self):
        for row in self._storage:
            yield tuple(row)

    @property
    def cols(self):
        for x in range(self.width):
            yield tuple(self[Coord(x, y)] for y in range(self.height))

    def itercoords(self) -> Generator[Coord, None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield Coord(x, y)


if __name__ == "__main__":
    data = Grid(2, 3)
    coord = Coord(1, 1)

    # __getitem__
    print(data[coord])

    # __setitem__
    data[coord] = 3
    print(data[coord])

    try:
        data[Coord(10, 20)] = 3
    except IndexError:
        pass

    try:
        data[Coord(-10, -20)] = 3
    except IndexError:
        pass

    # __contains__
    print("z" in data)
    print("a" in data)
    print(3 in data)

    # __len__
    print(len(data))

    # __iter__
    for x in data:
        print(x)

    # __str__
    print(data)

    # __repr__
    print(repr(data))
