#!/usr/bin/python

from device import *

class Database(Device):

    def __init__(self,name,oid,uri,cred={}):
        Device.__init__(self,name,oid)
        self.uri = uri
        self.cred = cred

    def query(self,query):
        raise NotImplementedError

class Clock(Device):

    def __init__(self):
        Device.__init__(self,'clock','0')

    def get(self,feat,val):
        if feat == 'time':
            return TIME.strftime('%I:%M')
