"""
There are no inlineCallbacks here. This code is just used to compare with a code with inlineCallbacks.
"""

from twisted.internet import reactor, defer

def someDeferredFunction():
    d = defer.Deferred()
    d.callback("Hi!")

    return d

def anotherDeferredFunction(result):
    d = defer.Deferred()
    d.addCallback(handleResult)
    d.callback("Hello! " + str(result))

    return d

def handleResult(result):
    print "handleResult result: " + str(result)

def functionWithAsyncProcesses():
    d = someDeferredFunction()
    d.addCallback(anotherDeferredFunction)

    return d

functionWithAsyncProcesses()
reactor.run()
