def Fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print('斐波那契数列的第10个数为:{}'.format(Fib(10)))
