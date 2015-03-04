#!/usr/bin/python

"""
[1] Establish a reasonable variety of devtypes
[!] Reconcile subclassing

[!] You need to redo Device class, make it more flexible but lower-level, closer to base object class
    (In respect to feats and vals)=
[!] Need to convert home-device-storing to sets
"""

class House(object):

    def __init__(self):
        self.users = {}
        self.devs = {}

        # self.add_dev(Clock())
        # self.add_dev(WeatherStation())

    def create_dev(self,name,Id):
        dev = Device(name,Id)
        self.add_dev(dev)
        return dev

    def add_dev(self,dev):
        self.devs[dev.get_name()] = dev

    def create_user(self,name):
        usr = User(self,name)
        self.add_user(usr)
        return usr

    def add_user(self,user):
        self.users[user.get_name()] = user

    def assign(self,dev,user):
        dev.add_owner(user)
        return self

    def get_dev(self,name):
        return self.devs.get(name)

    def get_devs_by_owner(self,user):
        devs = []
        for dev in self.devs:
            if user in dev.get_owners():
                devs.append(dev)
        return devs

    def get_devs_by_type(self,devtype):
        raise NotImplementedError

    def get_devs_by_name(self,devname):
        devs = []
        for dev in self.devs:
            if dev.name == devname or dev.devname == devname:
                devs.append(dev)
        return dev
