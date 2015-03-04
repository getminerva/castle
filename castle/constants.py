
import requests as RQST
import bluetooth as BLTH
import task as TASK
import time as TIME
import datetime as DTIME # Use timedelta and datetime classes for Signal interaction

###############################################################################
# Application Config
###############################################################################
DEBUG = False
OK = True
ERROR = False


ALWAYS = True
NEVER = False

QUERY_DELAY = 30

PRESENT = True
ABSENT = False

INVALID = -1
VALID = 0
WIP = 1
DONE = 2

BT = 0
WIFI = 1
RF = 2
X11 = 3
ON = 1
OFF = 0

class FileHandler(object):

    def __init__(self,fname,mode='r+'):
        self.fname = fname
        self.mode = mode
        self.f = None

        if not self._file_exists():
            self._create_file()

    def get_fname(self):
        return self.fname

    def _file_exists(self):
        try:
            f = open(self.fname,'r')
        except FileNotFoundError:
            return False
        f.close()
        return True

    def _create_file(self):
        try:
            f = open(self.fname,'x+')
        except FileExistsError:
            raise Error
        except PermissionError:
            raise Error
        f.close()
        return True

    def __enter__(self):
        self.f = open(self.fname,self.mode)
        return self.f

    def __exit__(self,*args):
        self.f.flush()
        self.f.close()
        del self.f
        self.f = None
        return None

class BadStuff(Exception):

    def __init__(self):
        pass

class CONX_START_FAIL(BadStuff):

    def __init__(self):
        BadStuff.__init__(self)

    def __str__(self):
        return '[-] Failed to establish connection.'
