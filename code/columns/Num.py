from code.util.Util import per
import math


class Num:
    """
    Default constructor that initialises:
    (a) countOfItems: To keep track of count of items inserted
    (b) columnName: current Sym Column Name
    (c) columnPosition: current Sym Column Position in the input dataset
    (d) numList: Dictionary to keep track of nums inserted & its count
    (e) lowestSeen: The lowest seen number in the dictionary
    (f) highestSeen: The highest seen number in the dictionary
    (g) isSorted: Is the data sorted or not
    """

    def __init__(self, colName='', colPos=0):
        self.countOfNums = 0
        self.columnName = colName
        self.columnPosition = colPos
        self.numList = {}
        self.lowestSeen = math.inf
        self.highestSeen = -math.inf
        self.isSorted = True  # no updates since last sort of data

    # Function to sort the numList
    def nums(self):
        print("Going to sort the numList")
        dict(sorted(self.numList.items()))
        return self.numList

    # Adds the passed num into numList
    def add(self, num):
        print("Going To add num:", num, "to the list of nums")
        numCount = self.numList.get(num, 0)
        self.countOfNums += 1
        self.lowestSeen = min(self.lowestSeen, num)
        self.highestSeen = max(self.highestSeen, num)
        self.numList[num] = numCount + 1
        print("Modified Num List:", self.numList, "with total nums =", self.countOfNums)

    # Calculate diversity (standard deviation for Nums, entropy for Sym)
    def div(self):
        a = self.nums()
        per1 = per(a, .9)
        per2 = per(a, .1)
        finalizer = per1 - per2
        return finalizer / 2.58

    # Calculating central tendency (median for Nums, mode for Sym)
    def mid(self):
        return per(self.nums(), .5)
