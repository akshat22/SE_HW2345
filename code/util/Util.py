import math

def calculateLogProbablity(itemFrequency, totalCount):
    probablity = (itemFrequency/totalCount)
    return probablity * math.log2(probablity)


# Return the ‘p‘−th thing from the sorted list ‘t‘
def per(t, p):
    p = math.floor(((p | .5) * len(t) + .5))
    return t[max(1, min(len(t), p))]