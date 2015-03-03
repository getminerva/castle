#!/usr/bin/python
"""


from core import *

def main():
    import time as T

    Home = House()
    Lamp = Home.create_dev('Lamp','00:11:08:01:06:17')

    def blink(dev,dur):
        dev.turn_on()
        T.delay(dur)
        dev.turn_off()

    def SOS(dev):
        with dev:
            blink(Lamp,3)
            blink(Lamp,3)
            blink(Lamp,3)
            blink(Lamp,9)
            blink(Lamp,9)
            blink(Lamp,9)
            blink(Lamp,3)
            blink(Lamp,3)
            blink(Lamp,3)

def main_thread():
    Home = HOME.House()
    Aria = System(Home)

    # Lamp = Home.create_dev('Lamp','00:11:08:01:06:17')

    TitaCherry = Home.create_user("Tita Cherry")
    TitaCherry.create_dev('Maria Rosario Chan\'s iPad','A4:D1:D2:8D:75:79')
    TitaCherry.create_dev('Maria Rosario Chan\'s iPhone',"gottagetheriphoneuuid")

    Me = Home.create_user('Joshua Paul Chan')
    Me.create_dev('Josh\'s HTC One M8','00:EE:BD:D3:2D:57')

    # my phone btaddr: 00:EE:BD:D3:2D:57
    # my phone IP address: 192.688.1.3

    # Light = BTDevice('Lamp','00:11:08:01:06:17',connect=True)

    # JustGotHere = Task(Aria.detect_entrance)
    # JustLeft = Task(Aria.detect_exit)
    # TurnItOn = Task(Light.turn_on)
    # TurnItOff = Task(Light.turn_off)
    # SayHi = Task(Aria.salute,TitaCherry)
    # SayBye = Task(Aria.valedict,TitaCherry)

    # Aria.users.append(TitaCherry)
    # Aria.add_link(JustGotHere,[TurnItOn,SayHi])
    # Aria.add_link(JustLeft,[TurnItOff,SayBye])

    # sched = SS.load_schedule('c:\\Users\\Joshua\\Documents\\GitHub\\CASTLE\\full_sched.xml')

    Aria.start()
    # Aria.salute(Me)

    # Time
    # What time is it?
    # It's {}

    # Weather
    # What's the weather like outside?
    # It's {qualitative_feeling}, {deg val} {deg unit} outside and {else}
    # Aria.say('The weather is 76 degrees outside.')

    # Television
    # What's on TV?
    # Loop: '{show} is on {network} [at {time}]'
    # Loop: '{show}, {show2} and {show3} are on {network}'

    most = 3

    # for n,ep in enumerate(sched.get_timeslot(DTIME.datetime.now())):
    #     if n > most:
    #         break
    #     show = ep.get_show()
    #     saystr = '{} is on {}'.format(show,show.get_network())
    #     Aria.say(saystr)

    while True:
        cmd = Aria.query_cmd()
        Aria.recv_cmd(cmd)

if __name__ == "__main__":
    main_thread()
    main()
