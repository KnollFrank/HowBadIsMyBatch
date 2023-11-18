def generatePairs(n):
    for i in range(n):
        for j in range(i):
            yield (i, j)
