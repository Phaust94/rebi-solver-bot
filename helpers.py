import itertools
import typing
import re

from constants import JOINERS, MAX_WORDS
from word import Word

__all__ = [
    "solve_rebus",
    "brute_force",
]


with open(r"russian.txt", "r", encoding="windows-1251") as f:
    DICTIONARY = f.readlines()

DICTIONARY = {x.lower().strip() for x in DICTIONARY}


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    ch = itertools.chain.from_iterable(
        itertools.combinations(s, r)
        for r in range(len(s)+1)
    )
    return ch


def parts_combinations(
        parts: typing.List[typing.List[Word]]
) -> typing.Generator[typing.Tuple[str], None, None]:
    n_parts = len(parts)
    for subset in itertools.product(*parts):
        for perm in itertools.permutations(subset, n_parts):
            for i, el in enumerate(perm):
                if not el.allowed_on_loc(i, n_parts - 1):
                    break
            else:
                # noinspection PyUnresolvedReferences
                yield tuple(x.text for x in perm)


def solve_rebus(options: str) -> str:
    parts = options.split("\n")
    parts = [
        [
            Word(word)
            for word in p.split(" ")
            if word.strip()
        ]
        for p in parts
    ]
    n_parts_wo_joiners = len(parts)
    parts.extend([JOINERS for _ in range(n_parts_wo_joiners - 1)])

    words = {
        "".join(perm): perm
        for perm in parts_combinations(parts)
    }

    inters = DICTIONARY.intersection(words)

    inters = sorted(inters)
    inters = inters[:MAX_WORDS]

    res = "\n".join(
        f"{k} <- {words[k]}"
        for k in inters
    )

    if not res:
        res = "No solutions found"

    return res


def brute_force(mask: str) -> str:
    matching_words = {
        w for w in DICTIONARY
        if re.findall(mask, w)
    }

    matching_words = sorted(matching_words)
    matching_words = matching_words[:MAX_WORDS]
    res = "\n".join(matching_words)
    return res
