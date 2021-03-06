"""
There are no inlineCallbacks here. This code is just used to compare with a code with inlineCallbacks.
"""

from twisted.internet import reactor, defer

def someDeferredFunction():
    d = defer.Deferred()
    d.callback("Hi!")

    return d

def handleResult(result):
    print "result: " + str(result)


def functionWithAsyncProcess():
    d = someDeferredFunction()
    d.addCallback(handleResult)

    return d

functionWithAsyncProcess()
reactor.run()
