#!/usr/bin/python

################################################################################
# Abstract Device classes
################################################################################

class Device(object):
    """
    Abstract Device Class
    This is the skeleton for all device classes.
    """

    def __init__(self, name, oid):
        self.name = name
        self.oid = oid
        self.owners = set()
        self.features = {"oid": oid, "name": name}

    def _read(self):
        raise NotImplementedError

    def _write(self):
        raise NotImplementedError

        @property
    def name(self):
        return self.name

        @property
    def Id(self):
        return self.oid

    def add_owner(self, user):
        if user not in self.owners:
            self.owners.add(user)

    def get_owners(self):
        return self.owners

    def rmv_owner(self, user):
        if user in self.owners:
            self.owners.remove(user)

    def get_feat(self, feat, *val):
        return self.features.get(feat)

    def set_feat(self, feat, val):
        raise NotImplementedError

    def _connect(self):
        raise NotImplementedError

    def _disconnect(self):
        raise NotImplementedError

    def __enter__(self):
        try:
            self.connect()
        except IOError:
            pass

    def __exit__(self):
        try:
            self.disconnect()
        except IOError:
            pass

    def __str__(self):
        return "< Device {}: \"{}\">".format(self.oid, self.name)

class Database(object):

    pass

class Result(object):
    '''
    An abstract result object.
    Results are generated from a device's actions - clocks return time results, weather returns temp/whatever results, etc.
    '''

    def __init__(self, text='', imgs=[]):
        raise NotImplementedError

################################################################################
# Communication Tunnel classes
################################################################################

class BTDevice(Device):
    """
    Bluetooth subclass of Device classes.
    Provides primitives for reading and writing as well as higher
    level operations.
    """

    def __init__(self, name, oid, addr=None, port=1):
        Device.__init__(self,name,oid)
        self.addr = addr
        self.port = port
        self.socket = BLTH.BluetoothSocket()

    def connect(self,port=None):
        try:
            if port == None:self.socket.connect((self.addr,self.port))
            self.socket.connect((self.addr,port))
        except IOError:
            print("Error establishing connection.")

    def _write(self,data):
        self.socket.send(data)

    def _read(self,chunk=1024):
        self.recv(chunk)

    def write(self,data):
        data = data.encode()
        self._write(data)
        return self._read(data).decode()

    def disconnect(self):
        self.socket.flush()
        self.socket.close()

    def set_feat(self,feature,val):
        feat = self.features.get(feature)
        if feat != None:
            #Physical setting update
            cmdstr = 'set:{}:{}'.format(feature,val)
            retcode = self.write(cmdstr)
            #Virtual setting update
            if retcode == OK:
                feat[feature] = val
        return self

    def get_feat(self,feature):
        return self.features.get(feature)

    def turn_on(self):
        self.set_feat('power',ON)

    def turn_off(self):
        self.set_feat('power',OFF)

    def start_stream(self):
        raise NotImplementedError

    def stop_stream(self):
        raise NotImplementedError

    def __getitem__(self,ind):
        return self.features.get(ind)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self):
        self.disconnect()


class WeatherStation(Database):
    default_uri = 'http://api.wunderground.com/api/key/features/settings/q/query.format'

    def __init__(self,uri='http://api.wunderground.com/api/c95b62a0f711a35f/{feat}/q/08854.json',cred=None):
        Database.__init__(self,'weather','1',uri,cred)

    def format(self,query):
        return self.uri.format(feat=query)

    def parse(self,result):
        content = result.json().get('current_observation')
        # print(content)
        realtemp = content.get('temperature_string')
        qual = content.get('weather')
        qualtemp = content.get('feelslike_string')
        resultstr = "It's {qual} outside. Temperature's {realtemp}, but it sort of feels like {qualtemp}.".format(qual=qual,realtemp=realtemp,qualtemp=qualtemp)
        return resultstr

    def query(self,feat):
        resp = RQST.get(self.format(feat))
        # print(resp)
        # print(resp.content)
        return self.parse(resp)

    def get(self,feat,val):
        return self.query(feat)

class TVScheduleWrapper(Device):

    def __init__(self,src):
        Device.__init__(self,'TV Schedule','2')
        self.features = {}

    def get(self,feat):
        raise NotImplementedError
