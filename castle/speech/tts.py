#!/user/bin/python

"""

TTS (Text-to-speech) module

Joshua Chan

USAGE:
cli:
>$ py tts "How was your day?"
I said, "How was your day?".

imported:
>>>import tts
>>>speaker = tts.Speaker()
>>>speaker.say("How was your day?")
I said, "How was your day?"
>>>
"""

class Speaker(object):

	def __init__(self):
		pass


	def speak(self, text):
		
