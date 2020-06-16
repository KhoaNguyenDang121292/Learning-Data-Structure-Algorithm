import random

filePath = "test_data.txt"
with open(filePath, 'w') as f:
    for i in range(0, 10000, +1):
        f.write(str(random.randint(0, 1000)))
        f.write(" ")