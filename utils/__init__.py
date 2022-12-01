from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from pprint import PrettyPrinter
from queue import PriorityQueue
import itertools as it
import more_itertools as mit
import numpy as np
import operator as op
import re

import os
import pathlib
import sys


NUMBER_RE = re.compile(r"\b\d+\b")
ALPHA_WORD_RE = re.compile(r"\b\w+\b")
WORD_RE = re.compile(r"\b\S+\b")


def input_text():
    target = pathlib.Path(
        os.environ.get("AOC_INPUT", sys.argv[1] if len(sys.argv) > 1 else "input.txt")
    )

    if not target.exists():
        print(
            "\033[1;31mError:\033[0m Input not found in either $AOC_INPUT, sys.argv[1] nor input.txt",
            file=sys.stderr,
        )
        exit(1)

    return target.read_text(encoding="utf8")


def input_nums():
    return list(map(int, NUMBER_RE.findall(input_text())))


def input_lines():
    return input_text().splitlines()


def input_lines_nums():
    return [list(map(int, NUMBER_RE.findall(l))) for l in input_lines()]


def input_words():
    return [ALPHA_WORD_RE.findall(l) for l in input_lines()]


def input_full_words() -> list[list[str]]:
    return [WORD_RE.findall(l) for l in input_lines()]


def list_int(it):
    return list(map(int, it))


def re_groups(regex, s):
    return re.match(regex, s).groups()
