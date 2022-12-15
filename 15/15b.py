from typing import Union
from utils import *
import multiprocessing

# Inclusive range (unoptimized)
@dataclasses.dataclass
class Range:
    start: int
    end: int

    def __and__(self, other: "Range") -> "Range":
        if self.is_empty or other.is_empty:
            return EMPTY_RANGE

        a, b = self, other
        if a.end > b.end:
            a, b = b, a

        if a.end < b.start:
            return EMPTY_RANGE
        elif a.start >= b.start:
            return a
        else:
            return Range(max(a.start, b.start), min(a.end, b.end))

    def __or__(self, other: "Range") -> "RangeSet":
        if (self & other).is_empty:
            return RangeSet([self, other])
        else:
            union = Range(min(self.start, other.start), max(self.end, other.end))
            return RangeSet([union])

    def __sub__(self, other: "Range") -> "RangeSet":
        intersection = self & other

        if intersection.is_empty:
            return RangeSet([self])
        else:
            left = Range(self.start, intersection.start - 1)
            right = Range(intersection.end + 1, self.end)
            return RangeSet([r for r in [left, right] if not r.is_empty])

    def __len__(self):
        if self.is_empty:
            return 0
        else:
            return self.end - self.start + 1

    @property
    def is_empty(self):
        return self.start > self.end

    def __bool__(self):
        return not self.is_empty


@dataclasses.dataclass
class RangeSet:
    ranges: list[Range]

    def __and__(self, other: Union[Range, "RangeSet"]) -> "RangeSet":
        if self.is_empty or other.is_empty:
            return EMPTY_RANGE_SET

        to_intersect = [other] if isinstance(other, Range) else other.ranges
        return RangeSet(
            functools.reduce(
                lambda rs, r2: [rint for r1 in rs if not (rint := r1 & r2).is_empty],
                to_intersect,
                self.ranges,
            )
        )

    def __sub__(self, other: Union[Range, "RangeSet"]) -> "RangeSet":
        to_diff = [other] if isinstance(other, Range) else other.ranges
        return RangeSet(
            functools.reduce(
                lambda rs, r2: [
                    rdiff for r1 in rs for rdiff in r1 - r2 if not rdiff.is_empty
                ],
                to_diff,
                self.ranges,
            )
        )

    def __or__(self, other: Union[Range, "RangeSet"]) -> "RangeSet":
        wrapped = RangeSet([other]) if isinstance(other, Range) else other
        return RangeSet(
            (self - wrapped).ranges + (wrapped - self).ranges + (self & other).ranges
        )

    @property
    def is_empty(self):
        return len(self.ranges) == 0

    def __iter__(self):
        return iter(self.ranges)


EMPTY_RANGE = Range(0, -1)
EMPTY_RANGE_SET = RangeSet([])

FOUR_MILLION = 4_000_000

MIN_R, MAX_R = 0, FOUR_MILLION
MIN_C, MAX_C = 0, FOUR_MILLION


def solve(search):
    for search_r in range(search[0], search[1] + 1):
        if search_r % 10_000 == 0:
            print(search_r)

        line_full = Range(MIN_C, MAX_C)

        for l in input_lines():
            sc, sr, bc, br = map(int, re.findall(r"-?\d+", l))
            maxd = abs(sc - bc) + abs(sr - br)

            minc = sc - maxd
            maxc = sc + maxd
            minr = sr - maxd
            maxr = sr + maxd

            if minr <= search_r <= maxr:
                line_diff = abs(sr - search_r)
                base_range = Range(minc + line_diff, maxc - line_diff)
                line_full -= base_range

        if (
            isinstance(line_full, RangeSet)
            and len(line_full.ranges)
            and (item := line_full.ranges[0])
            and item.start == item.end
        ):
            print("Solution:", item.start * 4_000_000 + search_r)
            break


BATCH_SIZE = 500_000
pool = multiprocessing.Pool(8)
pool.map(solve, [(i * BATCH_SIZE, (i + 1) * BATCH_SIZE) for i in range(8)])
