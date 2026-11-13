import re
from collections.abc import Callable

def normalize_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())

TRANSFORM: dict[str, Callable[[str], str]] = {
    "uppercase": str.upper,
    "lowercase": str.lower,
    "titlecase": str.title,
    "normalize-spaces": normalize_spaces
}