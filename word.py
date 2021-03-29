"""
Models a word class
"""

from dataclasses import dataclass
from functools import wraps

__all__ = [
    "Word", 'Joiner',
]


def change_init_signature(init):
    @wraps(init)
    def __init__(
            self,
            text: str,
            allowed_first: bool = True, allowed_last: bool = True
    ):
        init(self, text, allowed_first, allowed_last)
    return __init__


@dataclass(frozen=True)
class Word:
    __slots__ = ("text", "allowed_first", "allowed_last")

    text: str
    allowed_first: bool
    allowed_last: bool

    def __post_init__(self):
        object.__setattr__(self, 'text', self.text.lower().strip())

    def allowed_on_loc(self, cur_loc: int, max_loc: int) -> bool:
        allowed = True
        if cur_loc == 0 and not self.allowed_first:
            allowed = False
        elif cur_loc == max_loc and not self.allowed_last:
            allowed = False
        return allowed


Word.__init__ = change_init_signature(Word.__init__)
Word.__dataclass_fields__["allowed_first"].default = True
Word.__dataclass_fields__["allowed_last"].default = True


def change_init_signature_joiner(init):
    @wraps(init)
    def __init__(
            self,
            text: str,
            allowed_first: bool = True, allowed_last: bool = False
    ):
        init(self, text, allowed_first, allowed_last)
    return __init__


class Joiner(Word):
    __slots__ = ("text", "allowed_first", "allowed_last")


Joiner.__init__ = change_init_signature_joiner(Joiner.__init__)
Joiner.__dataclass_fields__["allowed_last"].default = False
