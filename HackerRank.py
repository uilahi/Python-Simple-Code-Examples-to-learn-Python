def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        b = a+b
        a = b



print(list(fibo(5)))