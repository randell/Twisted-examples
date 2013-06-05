from twisted.internet import reactor, defer

def someAsynchronousFunction():
    return defer.succeed("Hi!")

def handleResult(result):
    print "result: " + str(result)

d = someAsynchronousFunction()
d.addCallback(handleResult)

reactor.run()