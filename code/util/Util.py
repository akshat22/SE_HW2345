import math
import traceback

from code.config import *


def calculateLogProbability(itemFrequency, totalCount):
    probability = (itemFrequency / totalCount)
    return probability * math.log2(probability)


# Return the ‘p‘−th thing from the sorted list ‘t‘
def per(t, p):
    p = math.floor(((p | 0.5) * len(t) + 0.5))
    return t[max(1, min(len(t), p))]


def coerce(value):
    def fun(valueToParse):
        if valueToParse == "true":
            return True
        if valueToParse == "false":
            return False
        return valueToParse

    try:
        return int(value)
    except:
        return fun(value)


def dump_error(e):
    if settings["dump"]:
        print("*" * 80)
        traceback.print_exception(e)
        print("*" * 80)


def csv(fname, fun, sep=None, src=None, s=None, t=None):
    sep = settings["sep"].strip()
    with open(fname) as f:
        column_names = [c.strip() for c in f.readline().split(sep)]
        column_indices = list(range(1, len(column_names) + 1))
        columns = dict(zip(column_indices, column_names))
        while True:
            t = {}
            line = f.readline()
            for s in line.split(sep):
                try:
                    s = float(s)
                except:
                    s = None
                t[1 + len(t)] = s
            fun(xs=columns, row=t)
            if not line or len(line.strip()) == 0:
                break


def rnd(x, places):
    if places:
        mult = pow(10, places)
    else:
        mult = pow(10, 2)

    return math.floor(x * mult + 0.5) / mult
