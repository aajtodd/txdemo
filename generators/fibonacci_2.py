"""
Calculate the nth fibonacci using a generator
"""
import sys

def fib(n):
    fn, fn1 = 0, 1
    cnt = 0
    while True:
        if cnt > n:
            return
        yield fn
        fn, fn1 = fn1, fn + fn1
        cnt += 1


i = 0
gen = fib(12)
for x in gen:
    print("fib({0}): {1}".format(i, x))
    i += 1

# What would happen if we try to yield another value?
# x = next(gen)
# print(x)

