from twisted.internet import reactor, defer

def someCallback(result):
    print "result: " + str(result)
    raise RuntimeError, "whoops! we encountered an error"

def someErrback(failure):
    print "WTF"

d = defer.Deferred()
d.addCallback(someCallback)
d.addErrback(someErrback)
d.callback("Yarrr!")

reactor.run()