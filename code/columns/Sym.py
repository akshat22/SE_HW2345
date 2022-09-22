from code.util.Util import calculateLogProbability


class Sym:
    """
    Default constructor that initialises:
    (a) countOfItems(n): To keep track of count of items inserted
    (b) columnName(s): current Sym Column Name
    (c) columnPosition(c): current Sym Column Position in the input dataset
    (d) itemList(has): Dictionary to keep track of items inserted & its count
    """

    def __init__(self, colName='', colPos=0):
        self.countOfItems = 0
        self.columnName = colName
        self.columnPosition = colPos
        self.itemList = {}

    # Adds the passed item into ItemList
    def add(self, item):
        # print("Going To Add Item:", item, "to the list of items")
        itemCount = self.itemList.get(item, 0)
        self.countOfItems += 1
        self.itemList[item] = itemCount + 1
        # print("Modified Item List:", self.itemList, "with total items =", self.countOfItems)

    # Calculates Mode for the ItemList
    def mid(self):
        # print("Going to calculate Mode for the ItemList")
        maxFrequency = 0
        maxOccurringItem = ''
        for item, frequency in self.itemList.items():
            if maxFrequency < frequency:
                maxFrequency = frequency
                maxOccurringItem = item
        return maxOccurringItem

    # Calculates Entropy for the ItemList
    def div(self):
        # print("Going to calculate Entropy for the ItemList")
        entropy = 0
        for item, frequency in self.itemList.items():
            entropy -= calculateLogProbability(frequency, self.countOfItems)
        # print("Entropy =", entropy)
        return entropy
