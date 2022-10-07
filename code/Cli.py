import re
import sys

from code.util.Util import coerce

"""
Update settings from values on command−line flags. Booleans need no values
(we just flip the defaults).
"""

help = " \n\
        CSV : summarized csv file \n\
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n\
        USAGE: lua seen.lua [OPTIONS]\n\
        OPTIONS:\n\
        -e  --eg        start-up example                      = nothing\n\
        -d  --dump      on test failure, exit with stack dump = false\n\
        -f  --file      file with csv data                    = ../data/data.csv\n\
        -h  --help      show help                             = false\n\
        -n  --nums      number of nums to keep                = 512\n\
        -s  --seed      random number seed                    = 10019\n\
        -S  --seperator field seperator                       = , "

the = {}


class Cli:

    def __init__(self):
        self.pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
        re.sub(self.pattern, self.operation, help)
        self.cli(the)

    def operation(self, matchedRegex):
        key = matchedRegex.group(2)
        value = matchedRegex.group(3)
        the[key] = coerce(value)

    def cli(self, dictionary):
        for slot in dictionary:
            v = str(dictionary[slot])
            n = 0
            for arg in sys.argv:
                if n > 0:
                    if arg == "-" + slot[0] or arg == "--" + slot:
                        if v == "False":
                            v = "true"
                            dictionary[slot] = coerce(v)
                            continue
                        elif v == "True":
                            v = "false"
                            dictionary[slot] = coerce(v)
                            continue
                        else:
                            v = sys.argv[n + 1]
                        dictionary[slot] = coerce(v)
                n += 1
        print("The:", the)
        if dictionary["help"]:
            exit(help)
        return dictionary
