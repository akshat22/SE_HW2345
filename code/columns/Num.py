from code.util.Util import per
from code.config import *
import sys
import random
import math
import statistics


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
    (h) w : Not sure Yet
    """

    def __init__(self, colName='', colPos=0):
        self.countOfNums = 0
        self.columnName = colName
        self.columnPosition = colPos
        self.numList = {}
        self.lowestSeen = math.inf
        self.highestSeen = -math.inf
        self.isSorted = True  # no updates since last sort of data
        self.w = -1 if colPos and "-" in colPos else 1

    # Function to sort the numList
    def nums(self):
        print("\n Going to sort the numList \n")
        if not self.isSorted:
            self.numList.sort()
            self.isSorted = True
        return self.numList

    # Adds the passed num into numList
    def add(self, num):
        print("\n Going To add num:", num, "to the list of nums. \n")
        numCount = self.numList.get(num, 0)
        self.countOfNums += 1
        self.lowestSeen = min(self.lowestSeen, num)
        self.highestSeen = max(self.highestSeen, num)
        if len(self.numList) < settings["nums"]:
            self.numList[num] = numCount + 1
        else:
            pos = int(random.random() * 100) % len(self.numList)
            self.numList[pos] = num

        self.isSorted = False
        # print("Modified Num List:", self.numList, "with total nums =", self.countOfNums)

    # Calculate diversity (standard deviation for Nums, entropy for Sym)
    def div(self):
        print("\n Calculating the Standard Deviation:\n")
        a = self.nums()
        return (per(a, .9) - per(a, .1)) / 2.58

    # Calculating central tendency (median for Nums, mode for Sym)
    def mid(self):
        print("\n Calculating the central tendency:\n")
        return per(self.nums(), .5)