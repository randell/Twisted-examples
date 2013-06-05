from twisted.internet import reactor, defer

def someDeferredFunction():
    d = defer.Deferred()
    d.callback("Hi!")

    return d

def anotherDeferredFunction(result):
    d = defer.Deferred()
    d.callback("Hello! " + str(result))

    return d

def handleResult(result):
    print "handleResult result: " + str(result)

@defer.inlineCallbacks
def functionWithAsyncProcesses():
    result = yield someDeferredFunction()
    result2 = yield anotherDeferredFunction(result)
    handleResult(result2)

functionWithAsyncProcesses()
reactor.run()
