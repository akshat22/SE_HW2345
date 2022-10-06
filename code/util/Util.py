import math
from code import config
from contextlib import closing
import traceback

import requests
import codecs
import csv


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


def copy(t, u):
    pass


# Return the ‘p‘−th thing from the sorted list ‘t‘
def per(t, p):
    p = math.floor((p or 0.5) * len(t) + 0.5)
    return t[max(1, min(len(t), p)) - 1]


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


# Call ‘fun‘ on each row. Row cells are divided in ‘the.seperator‘
def csv_fun2(fileName, fun, n):
    sep = ','
    src = open(fileName)
    count = 0
    for line in src:
        t = []
        for s1 in line.rstrip().split(sep):
            t.append(coerce(s1))
        count = count + 1
        if n is False or (n is True and count <= 10):
            fun(t)


"""
Call `csvReader` on each row. Row cells are divided in `the.seperator`.
"""


def csvReader(fileName, fun, sep=None, src=None, s=None, t=None):
    sep = config.baseSettings["sep"].strip()
    with open(fileName) as f:
        column_names = [col.strip() for col in f.readline().split(sep)]
        column_indices = list(range(1, len(column_names) + 1))
        columns = dict(zip(column_indices, column_names))
        while True:
            dictionary = {}
            line = f.readline()
            for s in line.split(sep):
                try:
                    s = float(s)
                except:
                    s = None
                dictionary[1 + len(dictionary)] = s
            fun(xs=columns, row=dictionary)
            if not line or len(line.strip()) == 0:
                break


# Maths
def rnd(x, places):
    mult = 10 ** places
    return math.floor(x * mult + 0.5) / mult


def standard_dev(num):
    mean = sum(num) / len(num)
    std = (sum([((x - mean) ** 2) for x in num]) / len(num)) ** 0.5
    return round(std, 2)


def dump_error(error):
    if config.baseSettings["dump"]:
        print("*" * 70)
        traceback.print_exception(error)
        print("*" * 70)


def print_result(message, m, status):
    print(f"\n!!!!!\t{message}\t{m}\t{status}")
    print()
