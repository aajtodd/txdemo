"""
Calculate an infinite sequence of fibonacci numbers
"""

def fib():
    fn, fn1 = 0, 1
    while True:
        yield fn
        fn, fn1 = fn1, fn + fn1

fib_generator = fib()

i = 0
for x in fib_generator:
    print("fib({0}): {1}".format(i, x))
    i += 1
    # break to stay consistent with previous examples
    if i > 12:
        break

# we can keep going though
for i in xrange(13, 20):
    x = next(fib_generator)
    print(x)
