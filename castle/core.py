#!/usr/bin/python
"""
CASTLE Core

Joshua Chan
"""

import constants as CONST
BLTH = CONST.BLTH
TASK = CONST.TASK
THRD = CONST.TASK.THRD
DTIME = CONST.DTIME

import home as HOME
import subprocess as SBPRCS
#import texttospeech as TTS
import signalserver as SS

class System(THRD.Thread):

    def __init__(self,house):
        THRD.Thread.__init__(self)
        self.status = "READY"
        self.house = house
        self.links = set()

    def create_user(self,name):
        # [!] unlink households and users...
        return self.house.create_user(name)

    def create_link(self,trigger=None,tasks=[]):
        raise NotImplementedError

    def add_link(self,link):
        self.links.add(link)

    def run(self):
        """
        The system spawns a thread to monitor the
        presence of user devices."""
        ##for user in self.users:
            ##self.say("Finding {}...".format(user.name))
            ##if self.find(user):
                ##self.inhouse.append(user)
                ##pres_str = "{} is {}".format(user.get_name(),user.present)
                ##self.say(pres_str)
        while True:
            for link in self.links:
                for task in link.assess():
                    self.do(task)

            ##for user in self.users:
                ##now_here = self.find(user)
                  ##XOR gate yay
                ##if user.present ^ now_here:
                      ##self.status = "BUSY"
                    ##if now_here:
                        ##self.salute(user)
                    ##else:
                        ##self.valedict(user)
                    ##self.status = "READY"
                    ##user.present = now_here

    def do(self,task):
        return task.run()

    def show(self,result):
        """
        Show a result visually.
        """
        raise NotImplementedError

    def say(self,text):
        print(text)
        uri = 'http://translate.google.com/translate_tts?tl=en&q='
        link = uri + '+'.join(text.strip().split())
        SBPRCS.call(['ffplay','-hide_banner','-loglevel','quiet','-nodisp','-autoexit','-i',link])

    def parse_cmd(self,cmd):
        cmd = cmd.split(':')
        dev = cmd[1]
        action = cmd[2]
        feat = cmd[3]
        val = cmd[4] or None # Optional
        return {'dev':dev, 'action':action, 'feat':feat, 'val':val}

    def interpret_cmd(self,dictcmd):
        '''
        Take dictcmd and replace the strings with pointers to the actual instances.
        '''
        # dev replacing
        dictcmd['dev'] = self.search_devs(dictcmd.get('dev'))
        # action replacing
        if diccmd['action'] == 'get':
            dictcmd['action'] = dictcmd['dev'].get_action(dictcmd.get_feat('action'))
        return dictcmd

    def search_devs(self,name):
        return self.house.get_dev(name)

    def run_cmd(self,cmd):
        result = cmd['action'](cmd['feat'],cmd['val'])
        if result:
            speech = THRD.Thread(self.say(result))
            speech.run()
            # self.show(result)

    def recv_cmd(self, cmd):
        '''
        Queries cmd.
        parses cmd.
        interprets cmd.
        retrieves what cmd requests.
        executes requested item.
        '''
        dictcmd = self.parse_cmd(cmd)
        dictcmd = self.interpret_cmd(dictcmd)
        self.run_cmd(dictcmd)

    def query_cmd(self):
        '''
        Waits for cmds in form:
        cmd:dev:act:feat:val

        ex.
        cmd:sys:get:salute
        cmd:sys:get:valedict

        cmd:tv:get:sched:now
        cmd:sys:get:time
        '''
        cmd = input("Enter a cmd.\n").strip()
        return cmd

    def salute(self,user):
        text = "Welcome, {}".format(user.get_name()).strip('{}')
        self.say(text)

    def valedict(self,user):
        text = "Goodbye,{}".format(user.get_name()).strip('{}')
        self.say(text)

class Task(object):

    def __init__(self,target_func,*args,**kwargs):
        self.target_func = target_func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.kwargs == self.args == None:
            return self.target_func()
        elif self.kwargs == None:
            return self.target_func(*self.args)
        else:
            return self.target_func(*self.args,**self.kwargs)
        return None

class Link(object):

    def __init__(self,trigger=None,tasks=[]):
        self.trigger = trigger
        self.tasks = tasks

    def set_trigger(self,trigger_func):
        self.trigger = trigger_func

    def add_task(self,task_func):
        self.tasks.append(task_func)

    def set_tasks(self,tasks=[]):
        self.tasks = tasks

    def check_trigger(self):
        return self.trigger.run() == True

    def assess(self):
        if self.check_trigger():
            return True
        return False
