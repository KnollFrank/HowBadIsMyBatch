import itertools

def generatePairs(n):
    for i in range(n):
        for j in range(i):
            yield (i, j)

def take(iterable, numElements):
    return list(itertools.islice(iterable, numElements)) if numElements is not None else list(iterable)
