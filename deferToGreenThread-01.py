from twisted.internet import reactor

from eventlet.twistedutil import deferToGreenThread
from eventlet.twistedutil import join_reactor
from eventlet.green import httplib, urllib2

def http_request():
    request = urllib2.Request("http://randell.ph")
    result = urllib2.urlopen(request)
    return result.read()

def handleResult(result):
    print "result: " + str(result)

d = deferToGreenThread(http_request)
d.addCallback(handleResult)

reactor.run()