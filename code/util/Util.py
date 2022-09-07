import math
import sys


def calculateLogProbability(itemFrequency, totalCount):
    probability = (itemFrequency / totalCount)
    return probability * math.log2(probability)


# Return the ‘p‘−th thing from the sorted list ‘t‘
def per(t, p):
    p = math.floor(((p | .5) * len(t) + .5))
    return t[max(1, min(len(t), p))]


def coerce(self, s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1

    try:
        return int(s)
    except:
        return fun(s)


def cli(self, t):
    for slot in t:
        v = t[slot]
        v = str(v)
        n = 0
        for x in sys.argv:
            if n == 0:
                n += 1
                continue
            if x == "-" + slot[0] or x == "--" + slot:
                if v == "False":
                    v = "true"
                    t[slot] = self.coerce(v)
                    continue
                if v == "True":
                    v = "false"
                    t[slot] = self.coerce(v)
                    continue
                else:
                    v = sys.argv[n + 1]
                t[slot] = self.coerce(v)
            n += 1
    if t["help"]:
        exit(self.help)
    return t
