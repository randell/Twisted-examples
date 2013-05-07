"""
From: http://goo.gl/ok6NZ

"""
from twisted.internet import defer, reactor
from twisted.web.client import getPage

def listCallback(results):
    print results

def finish(ign):
    reactor.stop()

def test():
    d1 = getPage('http://www.google.com')
    d2 = getPage('http://randell.ph')
    dl = defer.DeferredList([d1, d2])
    dl.addCallback(listCallback)
    dl.addCallback(finish)

test()
reactor.run()