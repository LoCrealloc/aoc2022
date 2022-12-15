import re


def find_ints_strings(string: str) -> list[str]:
    return list(re.findall(r"\d+", string))


def find_ints(string: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", string)))
