from code.columns.Sym import Sym
from code.columns.Num import Num
from code.Cli import *

eg = {}


def runs(testName):
    if testName not in eg:
        return
    old = {}
    for t in the:
        old[t] = the[t]
    try:
        status = eg[testName]()
        if status==True:
            message = "PASS"
        elif status is None:
            message = "CRASH"
            status = False
        else:
            status = True
            message = "FAIL"
    except:
        status = False
        message = "CRASH"
    for t in old:
        the[t] = old[t]
    print("\n!!!!!", message, testName, status)
    print(("--" * 25))
    return status


def BAD():
    print("eg doesn't have this field")
    return


def LIST():
    testCaseNames = []
    for testCaseName in eg:
        testCaseNames.append(testCaseName)
    testCaseNames.sort()
    return testCaseNames


def LS():
    print("\nExamples lua csv −e ...")
    for k in LIST():
        print("\t" + k)
    return True

def ALL():
    failingTestCaseCount = 0
    testCasesList = LIST()
    for testCase in testCasesList:
        if testCase != "ALL":
            if not runs(testCase):
                failingTestCaseCount = failingTestCaseCount + 1
    # print('Total Testcases Failing after executing all testcase:', failingTestCaseCount)
    return True

def sym():
    symbol = Sym()
    symbols = ["a", "a", "a", "a", "b", "b", "c"]
    for x in symbols:
        symbol.add(x)
    mode = symbol.mid()
    entropy = symbol.div()
    # entropy = 1000 * entropy // 1 / 1000
    symDictionary = {"mid": mode, "div": entropy}
    print("\nSym Operation Results", symDictionary)
    # oo()
    return (mode == "a") and (1.37 <= entropy and entropy <= 1.38)


def num():
    numObject = Num()
    for i in range(1, 101):
        numObject.add(i)
    mid = numObject.mid()
    div = numObject.div()
    numDictionary = {'mid': mid, 'div': div}
    print("\nNum Operation Results", numDictionary)
    return (50 <= mid and mid <= 52) and (30.5 < div and div < 32)


def bignum():
    bignum = Num()
    the['nums'] = 32
    for i in range(1000):
        bignum.add(i + 1)
    return len(num._has) == 32

eg["BAD"]=BAD
eg["LIST"]=LIST
eg["LS"]=LS
eg["sym"] = sym
eg["num"] = num
eg["bignum"] = bignum
eg["ALL"] = ALL