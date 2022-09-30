from code.util.Util import per
from code import Cli as c
import random
import math


class Num:
    """
    Default constructor that initialises:
    (a) countOfNums(n): To keep track of count of items inserted
    (b) columnName(s): current Sym Column Name
    (c) columnPosition(c): current Sym Column Position in the input dataset
    (d) numList(_has): Dictionary to keep track of nums inserted & its count
    (e) lowestSeen(lo): The lowest seen number in the dictionary
    (f) highestSeen(hi): The highest seen number in the dictionary
    (g) isSorted: Is the data sorted or not
    (h) w : 1 or -1
    """

    def __init__(self, colName='', colPos=0):
        self.countOfNums = 0
        self.columnName = colName
        self.columnPosition = colPos
        self.numList = {}
        self.lowestSeen = math.inf
        self.highestSeen = -math.inf
        self.isSorted = True  # no updates since last sort of data
        if colName[-1] == '-':
            self.w = -1
        else:
            self.w = 1

    # Function to sort the numList
    def nums(self):
        # print("\n Going to sort the numList \n")
        if not self.isSorted:
            self.numList.sort()
            self.isSorted = True
        return self.numList

    # Adds the passed num into numList
    def add(self, num):
        # print("\n Going To add num:", num, "to the list of nums. \n")
        num = float(num)
        if num != "?":
            # numCount = self.numList.get(num, 0)
            self.countOfNums += 1
            self.lowestSeen = min(self.lowestSeen, num)
            self.highestSeen = max(self.highestSeen, num)
            if len(self.numList) < c.the["nums"]:
                pos = len(self.numList)
                self.numList[pos] = num
            elif random.random() < c.the["nums"] / self.countOfNums:
                pos = random.randrange(len(self.numList))
                self.numList[pos] = num
            self.isSorted = False
        # print("Modified Num List:", self.numList, "with total nums =", self.countOfNums)

    # Calculate diversity (standard deviation for Nums, entropy for Sym)
    def div(self):
        # print("\n Calculating the Standard Deviation:\n")
        a = self.nums()
        print("Div in nums:", (per(a, 0.9) - per(a, 0.1)) / 2.58)
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    # Calculating central tendency (median for Nums, mode for Sym)
    def mid(self):
        # print("\n Calculating the central tendency:\n")
        return per(self.nums(), 0.5)
