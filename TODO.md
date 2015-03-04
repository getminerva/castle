#TODO

SPEECH
/castle/speech/tts.py
[+] Wrote user spec/light doc-test for module in comment
[+] Look into text-preprocessing for speech? With accents and emphasis and what not
    [+] Looked into, is already part of the algorithms. Use TTS API in the short-run.
[+] Install ffmpeg (or some lightweight media player), place into bin...?
[+] Install venv to freeze things

DEVICE
/castle/device/device.py
[+] Rewrite Device classes to spearate comm. tunnels and devices themselves.


FRONTEND
[+] Add timestamp and heading [Done]
[+] Figure out why children divs that I've forced to float left make the parent div have a height of 0.
[+] Figure out how to use SVGs
    -Switch out the pngs

CORE
[+] Make import checker to prevent files from being imported multiple times
[+] Three separate sever instances working on three threads (or processes?)
    One would be for updates over BT, one Wifi, and the other for vocal..or nah
[+] Resolve dependencies and and reorganize/figure out importing for core and other nodes
[+] Template system for voice responses...? That would make it sorta flexible.
[+] Look into using decorators for storing tasks (and taskmaster) vs functools
[+] Clean up word-sorter



#WORKLOG
[+]
