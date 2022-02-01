def fib(n):
    p = 0
    q = 1
    while (p < n):
        yield p
        p, q = q, p + q
x = fib(10)
for i in fib(10):
  print(i)