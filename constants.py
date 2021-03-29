
from word import Joiner

__all__ = [
    "JOINERS",
    "MAX_WORDS",
]

JOINERS = {
    Joiner(""),
    Joiner("и", allowed_first=False),
    Joiner("да", allowed_first=False),
    Joiner("с"),
    Joiner("тоже", allowed_first=False),
    Joiner("что", allowed_first=False),
    Joiner("в"),
    Joiner("из"),
    Joiner("перед"),
    Joiner("пред"),
    Joiner("за"),
    Joiner("при"),
    Joiner("к"),
    Joiner("от"),
    Joiner("у"),
    Joiner("до"),
    Joiner("после"),
    Joiner("з"),
    Joiner("та", allowed_first=False),
    Joiner("енд", allowed_first=False),
    Joiner("энд", allowed_first=False),
    Joiner("на"),
    Joiner("над"),
    Joiner("по"),
    Joiner("под"),
}

MAX_WORDS = 50
