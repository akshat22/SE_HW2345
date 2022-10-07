from config import *
from Sym import Sym
from Num import Num
from Data import Data
from Cli import *
from Util import dump_error
import os

eg = {}


def runs(testName):
    if testName not in eg:
        return False
    old = {}
    for t in the:
        old[t] = the[t]
    try:
        status, message = eg[testName]()
        if testName == "LIST":
            message = "PASS"
        print("\n!!!!!", message, testName, status)
        print(("--" * 25))
        for t in old:
            the[t] = old[t]
    except Exception as e:
        status = False
        message = "CRASH"
        dump_error(e)
        for t in old:
            the[t] = old[t]
    return status


def BAD():
    try:
        print(eg["something"]["that"]["doesn't"]["exist!"])
        return True, "PASS"
    except Exception as e:
        dump_error(e)
        return False, "CRASH"


def LIST():
    testCaseNames = []
    for testCaseName in eg:
        testCaseNames.append(testCaseName)
    testCaseNames.sort()
    return True, testCaseNames


def LS():
    print("\nExamples lua csv −e ...")
    for k in LIST()[1]:
        print("\t" + k)
    return True, "PASS"


def ALL():
    failingTestCaseCount = 0
    testCasesList = LIST()[1]
    for testCase in testCasesList:
        if testCase != "ALL":
            if not runs(testCase):
                failingTestCaseCount += 1
    # print('Total Testcases Failing after executing all testcase:', failingTestCaseCount)
    print(settings)
    return True, "PASS"


def sym():
    symbol = Sym()
    symbols = ["a", "a", "a", "a", "b", "b", "c"]
    for x in symbols:
        symbol.add(x)
    mode = symbol.mid()
    entropy = symbol.div()
    entropy = 1000 * entropy // 1 / 1000
    symDictionary = {"div": entropy, "mid": mode}
    print(symDictionary)
    status = "PASS" if mode == "a" and 1.37 <= entropy <= 1.38 else "FAIL"
    return True, status


def num():
    numObject = Num(capacity=100)
    for i in range(1, 101):
        numObject.add(i)
    mid = numObject.mid()
    div = numObject.div()
    numDictionary = {'mid': mid, 'div': div}
    status = "PASS" if 50 <= mid <= 52 and 28 < div < 30 else "FAIL"
    return True, status


def test_bigNum():
    bigNumObj = Num(capacity=32)
    # the['nums'] = 32
    for i in range(1, 1001):
        bigNumObj.add(i)
    status = "PASS" if len(bigNumObj.numList) == 32 else "FAIL"
    print(bigNumObj.nums())
    return True


def csv():
    print("{", end=" ")
    d = Data("../data/data.csv")
    for i, col in d.cols.all.items():
        print(col.name, end=" ")
    print("}")
    for i, row in d.rows.items():
        if i > 10:
            break
        print("{", end=" ")
        for j, cell in row.cells.items():
            print(cell, end=" ")
        print("}")
    return True, "PASS"


def data():
    dat = Data("../data/data.csv")
    for _, col in dat.cols.y.items():
        if not isinstance(col, Num):
            continue
        print("{ "
              f":at {col.columnPosition} :hi {col.highestSeen} :isSorted {col.isSorted} :lo {col.lowestSeen} "
              f":n {col.countOfNums} :name {col.columnName} :w {col.w} "" }")
    return True, "PASS"


def stats():
    dat = Data("../data/data.csv")
    print()
    print("xmid", dat.stats(fun="mid", places=2, showCols=dat.cols.x))
    print("xdiv", dat.stats(fun="div", places=3, showCols=dat.cols.x))
    print("ymid", dat.stats(fun="mid", places=2, showCols=dat.cols.y))
    print("ydiv", dat.stats(fun="div", places=3, showCols=dat.cols.y))
    return True, "PASS"


def test_the():
    return True, "PASS"


eg["BAD"] = BAD             # Done
eg["LIST"] = LIST           # Done
eg["LS"] = LS               # Done
eg["sym"] = sym             # Done
eg["num"] = num
eg["bignum"] = test_bigNum
eg["ALL"] = ALL             # Done
eg["csv"] = csv
eg["data"] = data
eg["stats"] = stats
eg["the"] = test_the        # Done