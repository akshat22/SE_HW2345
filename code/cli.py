import re
import sys

from code.util.Util import coerce

"""
Update settings from values on command−line flags. Booleans need no values
(we just flip the defaults).
"""


class Cli:

    def __init__(self) -> None:
        self.the = {}
        self.help = " \n\
        CSV : summarized csv file \n\
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n\
        USAGE: lua seen.lua [OPTIONS]\n\
        OPTIONS:\n\
        -e  --eg        start-up example                      = nothing\n\
        -d  --dump      on test failure, exit with stack dump = false\n\
        -f  --file      file with csv data                    = ../data/auto93.csv\n\
        -h  --help      show help                             = false\n\
        -n  --nums      number of nums to keep                = 512\n\
        -s  --seed      random number seed                    = 10019\n\
        -S  --seperator field seperator                       = , "
        self.pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
        re.sub(self.pattern, self.operation, self.help)

    def operation(self, match):
        k = match.group(2)
        x = match.group(3)
        self.the[k] = coerce(x)
