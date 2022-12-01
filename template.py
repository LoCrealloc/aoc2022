# Inspired by Defelo https://github.com/Defelo/AdventOfCode

from datetime import date

import pyperclip

import aoc
import re
from collections import deque

def ans(answer):
    print(answer)
    pyperclip.copy(str(answer))


year, day = (t := date.today()).year, t.day

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")




ans()