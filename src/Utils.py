def fillLsts(lsts, desiredLen, fillValue):
    return [fillLst(lst, desiredLen, fillValue) for lst in lsts]


def fillLst(lst, desiredLen, fillValue):
    return lst + [fillValue] * (max(desiredLen - len(lst), 0))


def flatten(tuples):
    return [item for tuple in tuples for item in tuple]


def get_dictWithKeys_dictWithoutKeys(dict, keys):
    dictWithKeys = {key: dict[key] for key in keys}
    dictWithoutKeys = {key: dict[key] for key in dict.keys() - keys}
    return dictWithKeys, dictWithoutKeys
