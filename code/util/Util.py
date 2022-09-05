import math

def calculateLogProbablity(itemFrequency, totalCount):
    probablity = (itemFrequency/totalCount)
    return probablity * math.log2(probablity)