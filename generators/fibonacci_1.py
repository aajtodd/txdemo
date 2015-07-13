"""
First n fibonacci numbers using iteration/list
"""

def fib(n):
    """
    Calculate the nth Fibonacci number
    """
    fn, fn1 = 0, 1
    for i in xrange(n):
        fn, fn1 = fn1, fn + fn1
    return fn

for i in xrange(13):
    print("fib({0}): {1}".format(i, fib(i)))
