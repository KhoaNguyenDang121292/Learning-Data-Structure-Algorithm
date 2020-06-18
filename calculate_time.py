import timeit

def CalculateTime(functionName):
    return timeit.timeit(functionName, number=100000)