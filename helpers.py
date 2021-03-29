import itertools
import typing

from constants import JOINERS

__all__ = [
    "solve_rebus",
]


with open(r"russian.txt", "r", encoding="windows-1251") as f:
    DICTIONARY = f.readlines()

DICTIONARY = {x.strip().lower() for x in DICTIONARY}


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
        parts: typing.List[typing.List[str]]
) -> typing.Generator[typing.Tuple[str], None, None]:
    n_parts = len(parts)
    for subset in itertools.product(*parts):
        for perm in itertools.permutations(subset, n_parts):
            # noinspection PyUnresolvedReferences
            yield tuple(x.lower() for x in perm)


def solve_rebus(options: str) -> str:
    parts = options.split("\n")
    parts = [p.split(" ") for p in parts]
    n_parts_wo_joiners = len(parts)
    parts.extend([JOINERS for _ in range(n_parts_wo_joiners - 1)])

    words = {
        "".join(perm): perm
        for perm in parts_combinations(parts)
    }

    inters = DICTIONARY.intersection(words)

    res = "\n".join(
        f"{k} <- {words[k]}"
        for k in inters
    )

    if not res:
        res = "No solutions found"

    return res
