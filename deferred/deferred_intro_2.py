"""
Deferred intro re-written with inline callbacks
"""
import time
from twisted.internet.defer import inlineCallbacks, Deferred
from twisted.internet import reactor

def delayed_call(ready_future):
    now = time.time()
    ready_future.callback(now)

def async_call(delay):
    on_ready = Deferred()
    reactor.callLater(delay, delayed_call, on_ready)
    return on_ready


@inlineCallbacks
def foo():
    now = time.time()
    print("foo - before async call: {0}".format(now))
    later = yield async_call(3)
    print("foo - after async call: {0}".format(later))

@inlineCallbacks
def bar():
    now = time.time()
    print("bar - before async call: {0}".format(now))
    later = yield async_call(1.5)
    print("bar - after async call: {0}".format(later))


if __name__ == '__main__':
    reactor.callWhenRunning(foo)
    reactor.callWhenRunning(bar)
    reactor.callLater(5, reactor.stop)
    reactor.run()
