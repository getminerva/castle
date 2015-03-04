##
__name__ = "Task"
__version__ = 2.0
__author__ = "Joshua Paul A. Chan"
__description__ = """
{} {} by {}

This is a threading framework for task and task handling.

s: 4/13/14
t:
e: 7/18/14
""".format(__name__,__version__,__author__)

###NOTES
"""
[+] 4/13: Making Task_Handler run on its own thread, basically to tell it to do something
    now you use the tell_todo (or add task) func and it adds that task (func,args,kwargs)
    to its queue, which then
[+]7/18: Used functools for a somewhat obtuse but workable situation.
    Renamed Task_Handler to Handler.

[!] Reconcile the target_func arguments (so you can really accept any func)
    THOUGHT: Maybe use/look decorators?

"""
###

import threading as THRD
import functools as FUNC
import queue as Q

class Handler(THRD.Thread):
    """
    Task Handler class.
    Works by having a task queue and current task queue.
    When you tell it to do a task, it adds it to the queue and
    continually works to move items from its queue to current task queue.
    """

    def __init__(self,qsize=0,tasksize=0,*args,**kwargs):
        THRD.Thread.__init__(self,*args,**kwargs)
        self.qtasks = Q.Queue(qsize)
        self.curtasks = Q.Queue(tasksize)

    def _do(self,func,*args,**kwargs):
        result = Task(self,func,*args,**kwargs).start()
        return result

    def do_task(self,info):
        self._do(info[0],info[1],info[2])
        return self

    def do(self,func,*args,**kwargs):
        self.qtasks.put((func,args,kwargs))

    def stop(self,func):
        for task in self.curtasks:
            if func == task.target_func:
                task.target_func = task.dud #Switches, not stops, the thread's func.
        return self

    def run(self):
        while True:
            if not (self.qtasks.empty() and self.curtasks.full()):
                self.curtasks.put(self.qtasks.get())
                self.qtasks.task_done() #Garbage cleanup
            #currently, it fills up curtasks/empties queue THEN empties curtasks
            while not self.curtasks.empty():
                self.do_task(self.curtasks.get())

    def __del__(self):
        while not self.curtasks.empty():
            self.curtasks.get().task_done()
        while not self.qtasks.empty():
            self.qtasks.get().task_done()

class Task(THRD.Thread):

    def __init__(self,master,target_func,*func_args,**func_kwargs):
        THRD.Thread.__init__(self)
        self.setDaemon = True
        self.master = master
        self.func = FUNC.partial(target_func,*func_args,**func_kwargs)

    def dud(self,*args,**kwargs):
        pass

    def run(self):
        result = self.func()
        print("Task done.")
        self.master.curtasks.task_done()
        return result

def main():

    def test_func1(*args,**kwargs):
        print("No argument functions are good!")
        return None

    def test_func2(text,*args,**kwargs):
        print("As are functions with:\n specified params: {}\n*args: {}\n\
**kwargs: {}".format(text,args,kwargs))
        return None

    def test_func3(tdelay):
        print("Delays of {} are cool too!".format(tdelay))
        return None

    Manager = Handler()
    Manager.start()

    try:Manager.do(test_func1)
    except:print("Functions need params.")

    try:Manager.do(test_func2,"[TEXT HERE]","1","2","3",more="A",other="B",n="C")
    except:print("Functions specified params and args merge.")
    #Nah, still not a pretty/simple way to do it..
    #Manager.do(test_func3,3,3)

    #[1]All functions being created for task need to accept *args and **kwargs
    #[2]They can only access kwd parameters from **kwargs

if __name__ == "__main__":
    main()
