from typing import Union
from utils import *

LINE = 2000000

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

values = RangeSet([])
for l in input_lines():
    sc, sr, bc, br = map(int, re.findall(r"-?\d+", l))
    maxd = abs(sc - bc) + abs(sr - br)

    minc = sc - maxd
    maxc = sc + maxd
    minr = sr - maxd
    maxr = sr + maxd

    if minr <= LINE <= maxr:
        line_diff = abs(sr - LINE)
        base_range = Range(minc + line_diff, maxc - line_diff)

        if br == LINE:
            values |= base_range - Range(bc, bc)
        else:
            values |= base_range

print(sum(map(len, values)))
