def fibonacciLoop(n):
    fib0 = 0
    fib1 = 1
    next = fib0 + fib1
    if n == 0:
        return fib0
    elif n == 1:
        return fib1
    else:
        for i in range(2, n, +1):
            fib0 = fib1
            fib1 = next
            next = fib0 + fib1
    return next

def fibonacciRecursive(n):
    if n < 0:
        return -1
    # Base case
    elif n == 0: 
        return 0
    # Base case
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

if __name__ == "__main__":
    n = 4
    result = fibonacciRecursive(n)
    print("Fib: " + str(result))