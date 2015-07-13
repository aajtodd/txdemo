"""
Toy example showing how to send values to a generator
"""

def gen(n):
    x = n
    cnt = 0
    while True:
        if x == n:
            result = yield cnt
            print("generator recv'd: %s" % result)
            x = 0
            cnt += 1
        x += 1

g = gen(10)
g.send(None)  # start the generator
for i in xrange(3):
    print("generator yielded: %s" % g.send(i*10))


