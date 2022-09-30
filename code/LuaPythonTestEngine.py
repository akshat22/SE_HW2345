from random import random

from code.columns.Sym import Sym
from code.columns.Num import Num
from code.columns import Data
from code.util import Util as uti
from code.Cli import *


class LuaPythonTestEngine:

    def __init__(self):
        self.message = 'Hello everyone'

    def the(self):
        print(the)
        return True

    def csv(self):
        n = True
        uti.csv_fun2('../hw2test.csv', self.csvOutput, n)
        return True

    def csvOutput(self, row):
        print(row)

    def runs(self, k):
        if k not in self.eg.keys():
            print('returning')
            return

        the['seed'] = random.random()
        old = {}
        for a, b in the.items():
            old[a] = b
        status, out = False, False
        if the['dump']:
            status = True
            out = self.eg[k](self)
        else:
            try:
                out = self.eg[k](self)
            except:
                status = False

        for x, y in old.items():
            the[x] = y

        msg = ("PASS" if out else "FAIL") if status else "CRASH"
        print("!!!!!!\t" + msg + "\t" + k + "\t" + str(status))
        return out

    def BAD(self):
        print("eg doesn't have this field")
        return

    def LIST(self):
        testCaseNames = []
        for testCaseName in self.eg:
            testCaseNames.append(testCaseName)
        testCaseNames.sort()
        return testCaseNames

    # def LS(self):
    #     print("\nExamples lua csv −e ...")
    #     for k in LIST():
    #         print("\t" + k)
    #     return True

    # def ALL(self):
    #     failingTestCaseCount = 0
    #     testCasesList = LIST()
    #     for testCase in testCasesList:
    #         if testCase != "ALL":
    #             if not runs(testCase):
    #                 failingTestCaseCount = failingTestCaseCount + 1
    #     # print('Total Testcases Failing after executing all testcase:', failingTestCaseCount)
    #     return True

    def sym(self):
        symbol = Sym(colName="Sym")
        symbols = ["a", "a", "a", "a", "b", "b", "c"]
        for x in symbols:
            symbol.add(x)
        mode = symbol.mid()
        entropy = symbol.div()
        # entropy = 1000 * entropy // 1 / 1000
        symDictionary = {"mid": mode, "div": entropy}
        print("\nSym Operation Results", symDictionary)
        return (mode == "a") and (1.37 <= entropy <= 1.38)

    def num(self):
        numObject = Num(colName="Num")
        for i in range(1, 101):
            numObject.add(i)
        mid = numObject.mid()
        div = numObject.div()
        numDictionary = {'mid': mid, 'div': div}
        print("\nNum Operation Results", numDictionary)
        return (50 <= mid <= 52) and (30.5 < div < 32)

    def bigNum(self):
        bigNumObject = Num(colName="BigNum")
        the['nums'] = 32
        for i in range(1000):
            bigNumObject.add(i + 1)
        return len(bigNumObject.numList) == 32

    def statsMid(self, col):
        return col.mid()

    def statsDiversity(self, col):
        return col.div()

    def data(self):
        dat = Data(src='../hw2test.csv')
        for col in dat.cols.y:
            print(col.__string__())
        return True

    def stats(self):
        data = Data(src='../hw2test.csv')

        print(data.stats(2, data.cols.x, self.statsMid))
        print(data.stats(3, data.cols.x, self.statsDiversity))
        print(data.stats(2, data.cols.y, self.statsMid))
        print(data.stats(3, data.cols.y, self.statsDiversity))
        return True

    eg = {'the': the, "num": num, "bignum": bigNum, "sym": sym, "csv": csv, "data": data, "stats": stats}
    fails = 0

    def all(self):
        for k in sorted(self.eg.keys()):
            print(k)
            if not self.runs(k):
                self.fails += 1
        return True


testCall = LuaPythonTestEngine()
testCall.all()
