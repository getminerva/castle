#TODO

SPEECH

DEVICE

/castle/device/device.py
[+] Rewrite Device classes to spearate comm. tunnels and devices themselves.

/fridge.py
[+] Move to ./castle?


FRONTEND
[+] Remove results log and restyle bar
	Add animations
[+] Move frontend to the inside?

CORE
[+] Make import checker to prevent files from being imported multiple times
[+] Three separate sever instances working on three threads (or processes?)
    One would be for updates over BT, one Wifi, and the other for vocal..or nah
[+] Resolve dependencies and and reorganize/figure out importing for core and other nodes
[+] Template system for voice responses...? That would make it sorta flexible.
[+] Look into using decorators for storing tasks (and taskmaster) vs functools
[+] Clean up word-sorter



#WORKLOG

3/4/2015

/castle/speech/tts.py

    [+] Wrote user spec/light doc-test for module in comment
    [+] Look into text-preprocessing for speech? With accents and emphasis and what not
        [+] Looked into, is already part of the algorithms. Use TTS API in the short-run.
    [+] Install ffmpeg (or some lightweight media player), place into bin...?
    [+] Install venv to freeze things

/frontend/index.html

	[+] Add timestamp and heading [Done]
	[+] Figure out why children divs that I've forced to float left make the parent div have a height of 0
		They float out of the container, and need overflow: hidden for the container to be the right size
		[Done]
	[+] Figure out how to use SVGs
		-Switch out the pngs
