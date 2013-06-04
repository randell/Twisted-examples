from twisted.internet import reactor, defer

def handleResult(result):
    print "result: " + str(result)

d = defer.Deferred()
d.addCallback(handleResult)
d.callback("Yarrr!")

reactor.run()