from twisted.internet import reactor, defer
from twisted.internet.defer import inlineCallbacks

def someDeferredFunction():
    d = defer.Deferred()
    d.callback("Hi!")

    return d

def handleResult(result):
    print "result: " + str(result)

@inlineCallbacks
def functionWithAsyncProcess():
    result = yield someDeferredFunction()
    handleResult(result)

functionWithAsyncProcess()
reactor.run()