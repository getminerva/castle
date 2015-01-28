#!/usr/bin/python

class User(object):

    def __init__(self,oid,name,home):
        self.oid = oid
        self.name = name
        self.loc = {}
        self.home = home

    def create_dev(self,name,Id):
        mydev =  self.home.create_dev(name,Id)
        self.home.assign(mydev,self)
        return mydev

    def get_devs(self):
        return self.home.get_devs_by_owner(self)

    def get_loc(self):
        return self.loc

    def get_name(self):
        return self.name

    def __str__(self):
        return "< User {}: \"{}\">".format(self.oid,self.name)
