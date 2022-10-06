from code.columns.Sym import Sym
from code.columns.Num import Num
from code.columns.Data import Data
from code import config
from code.util import Util as uti
from main import the

eg = {}
fails = 0


def test_the():
    print("*" * 50)
    print(the)
    return True, "PASS"


def test_csv():
    """Show we can read csv files."""
    print("{", end=" ")
    datad = Data("../data/data.csv")
    for i, col in datad.cols.all.items():
        print(col.name, end=" ")
    print("}")
    for i, row in datad.rows.items():
        if i > 10:
            break
        print("{", end=" ")
        for j, cell in row.cells.items():
            print(cell, end=" ")
        print("}")

    return True, "PASS"


def runs(k):
    try:
        old_settings = config.baseSettings
        if not eg[k]:
            return False
        status, message = eg[k]()
        if k == "LIST":
            message = "PASS"
        uti.print_result(message, k, status)
        config.baseSettings = old_settings
        """restore old settings"""
    except Exception as e:
        status = False
        message = "CRASH"
        uti.dump_error(e)
        uti.print_result("CRASH", k, False)
    return status


def bad(self):
    try:
        print("eg doesn't have this field")
        return True, "PASS"
    except Exception as e:
        uti.dump_error(e)
        return False, "CRASH"


def LIST():
    testCaseNames = []
    for testCaseName in eg:
        testCaseNames.append(testCaseName)
    testCaseNames.sort()
    return testCaseNames, "PASS"


def ls():
    print("\nExamples lua csv −e ...")
    for k in LIST():
        print("\t" + k)
    return True, "PASS"


def ALL():
    failingTestCaseCount = 0
    testCasesList = LIST()
    for testCase in testCasesList:
        if testCase != "ALL":
            if not runs(testCase):
                failingTestCaseCount = failingTestCaseCount + 1
    # print('Total Testcases Failing after executing all testcase:', failingTestCaseCount)
    return True, "PASS"


def sym():
    symbol = Sym()
    symbols = ["a", "a", "a", "a", "b", "b", "c"]
    for x in symbols:
        symbol.add(x)
    mode = symbol.mid()
    entropy = symbol.div()
    entropy = 1000 * entropy // 1 / 1000
    symDictionary = {"mid": mode, "div": entropy}
    print("\nSym Operation Results", symDictionary)
    return (mode == "a") and (1.37 <= entropy <= 1.38)


def num():
    numObject = Num(capacity=100)
    for i in range(1, 101):
        numObject.add(i)
    mid = numObject.mid()
    div = numObject.div()
    numDictionary = {'mid': mid, 'div': div}
    print("\nNum Operation Results", numDictionary)
    return (50 <= mid <= 52) and (30.5 < div < 32)


def bigNum():
    bigNumObject = Num(capacity=32)
    # the['nums'] = 32
    for i in range(1000):
        bigNumObject.add(i + 1)
    return len(bigNumObject.numList) == 32


def data():
    dat = Data(src='../data/data.csv')
    for _, col in dat.cols.y.items():
        if not isinstance(col, Num):
            continue
        print("{ " + f":at {col.columnPosition} :hi {col.highestSeen} :isSorted {col.isSorted} :lo {col.lowestSeen}"
                     f" :n {col.countOfNums} :name {col.columnName} :w {col.w}" + " }")
    return True


def stats(self):
    dat = Data(src='../data/data.csv')
    print()
    print("xmid", dat.stats(fun="mid", places=2, showCols=dat.cols.x))
    print("xdiv", dat.stats(fun="div", places=3, showCols=dat.cols.x))
    print("ymid", dat.stats(fun="mid", places=2, showCols=dat.cols.y))
    print("ydiv", dat.stats(fun="div", places=3, showCols=dat.cols.y))
    return True


eg["BAD"] = bad
eg["ALL"] = all
eg["LIST"] = list
eg["LS"] = ls
eg["bignum"] = bigNum
eg["csv"] = test_csv
eg["data"] = data
eg["num"] = num
eg["stats"] = stats
eg["the"] = test_the
eg["sym"] = sym
