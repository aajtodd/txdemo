"""
Introduction to Deferred/Futures
"""
import time
from twisted.internet.defer import Deferred
from twisted.internet import reactor

def delayed_call(ready_future):
    now = time.time()
    ready_future.callback(now)

def async_call(delay):
    """
    Simulate an asyncronous call, returns a deferred that will be
    resolved after the delay time
    :param delay: The delay to simulate in seconds (e.g. 2.5)
    :return: Deferred
    """
    on_ready = Deferred()
    reactor.callLater(delay, delayed_call, on_ready)
    return on_ready

def continue_processing(timestamp, from_func):
    print("{0} - after async call: {1}".format(from_func, timestamp))


def foo():
    now = time.time()
    print("foo - before async call: {0}".format(now))
    future = async_call(3)
    # Call the contine_processing function when done and pass an extra argument 'foo'
    future.addCallback(continue_processing, 'foo')

def bar():
    now = time.time()
    print("bar - before async call: {0}".format(now))
    future = async_call(1.5)
    future.addCallback(continue_processing, 'bar')


if __name__ == '__main__':
    reactor.callWhenRunning(foo)
    reactor.callWhenRunning(bar)
    reactor.callLater(5, reactor.stop)
    reactor.run()
