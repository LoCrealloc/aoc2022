import re


def find_ints(string: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", string)))
