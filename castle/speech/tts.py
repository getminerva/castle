#!/user/bin/python

"""

TTS (Text-to-speech) module

Joshua Chan

USAGE:
cli:
>$ py tts "How was your day?"
I said, "How was your day?".
>$

imported:
>>>import tts
>>>speaker = tts.Speaker()
>>>speaker.say("How was your day?")
I said, "How was your day?"
>>>
"""

# import some audio module or cmd thing
import subprocess # to open ffmpeg from bin

# Use some TTS service before I roll my own
import requests # to make internet call

import queue # to hold texts to say
# Process
# import numpy # to do necessary numerical computations

class Speaker(object):
	"""
	Explanation about the speaker object
	"""

	def __init__(self):
		max_sents = 12
		self.q = queue.Queue(max_sents) # Holds the text queue
		pass

	def get_queue(self):
		"""
		Return an immutable view of the text queue.
		"""
		raise NotImplementedError
		return self

	def say(self, text):
		"""
		Takes text and speaks it.

		Puts it through a pre-processor and (temporarily) hits the TTS API with it.
		"""
		uri = "http://tts-api.com/tts.mp3"
		query = "q=hello+world"

		raise NotImplementedError
		return self

	def _say(self, audio_data):
		# Spawn subprocess of fmmpeg
		# Pop speech from Q, blocks
		# Pipes text to ffmpeg
		# When ffmpeg finishes, unblock Q
		return self
