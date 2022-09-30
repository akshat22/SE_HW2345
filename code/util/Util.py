import math
import sys
from contextlib import closing
import requests
import codecs
import csv

def calculateLogProbability(itemFrequency, totalCount):
    probability = (itemFrequency / totalCount)
    return probability * math.log2(probability)

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

def cli(dictionary):
    for slot in dictionary:
        v = dictionary[slot]
        v = str(v)
        n = 0
        for x in sys.argv:
            if n == 0:
                n += 1
                continue
            if x == "-" + slot[0] or x == "--" + slot:
                if v == "False":
                    v = "true"
                    dictionary[slot] = self.coerce(v)
                    continue
                if v == "True":
                    v = "false"
                    dictionary[slot] = self.coerce(v)
                    continue
                else:
                    v = sys.argv[n + 1]
            dictionary[slot] = self.coerce(v)
            n += 1
    if dictionary["help"]:
        exit(self.help)
    return dictionary

def copy(t, u):
    pass

# Return the ‘p‘−th thing from the sorted list ‘t‘
def per(t, p):
    p = math.floor(((p | 0.5) * len(t) + 0.5))
    return t[max(1, min(len(t), p))]

def push(t, x):
    t.append(x)
    return x

def csv_fun(url):
    row_list1 = []
    url = url
    with closing(requests.get(url, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        for row in reader:
            for cell in row:
                temp = row.index(cell)
                temp1 = coerce(cell)
                row[temp] = temp1
            row_list1.append(row)
    return row_list1

# Maths
def rnd(x, places):
    mult = 10 ** places
    return math.floor(x * mult + 0.5) / mult