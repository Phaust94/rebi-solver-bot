"""
Models a word class
"""

from dataclasses import dataclass, field

__all__ = [
    "Word", 'Joiner',
]


@dataclass
class Word:
    __slots__ = ("text", "allowed_first", "allowed_last")

    text: str
    allowed_first: bool = field(default=True)
    allowed_last: bool = field(default=True)

    def __post_init__(self):
        self.text = self.text.lower().strip()

    def allowed_on_loc(self, cur_loc: int, max_loc: int) -> bool:
        allowed = True
        if cur_loc == 0 and not self.allowed_first:
            allowed = False
        elif cur_loc == max_loc and not self.allowed_last:
            allowed = False
        return allowed


class Joiner(Word):
    allowed_last: bool = field(default=False)
