def fillLsts(lsts, desiredLen, fillValue):
    return [fillLst(lst, desiredLen, fillValue) for lst in lsts]


def fillLst(lst, desiredLen, fillValue):
    return lst + [fillValue] * (max(desiredLen - len(lst), 0))
