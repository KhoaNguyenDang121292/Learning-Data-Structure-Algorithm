def ReadSampleData():
    with open("test_data.txt", "r") as f:
        arr = f.readline().split()
        arr = list(map(int, arr))
    return arr