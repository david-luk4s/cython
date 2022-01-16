def fib(n):
    a=0
    b=0

    for i in range(n):
        a, b = a + b, a

    return a