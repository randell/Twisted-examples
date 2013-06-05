from twisted.internet import reactor, defer

def someDeferredFunction():
    return defer.succeed("Hi!")

def handleResult(result):
    print "result: " + str(result)

d = someDeferredFunction()
d.addCallback(handleResult)

reactor.run()