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
>>>Morgan_Freeman = tts.Speaker()
>>>Morgan_Freeman.say("How was your day?")
I said, "How was your day?"
>>>
"""

# import some audio module or cmd thing
import subprocess # to open ffmpeg from bin

# Use some TTS service before I roll my own
import requests # to make API call

import queue # to hold texts to say

# Process
# import numpy # to do necessary numerical computations

class Speaker(object):
	"""
	Explanation about the speaker object
	"""

	def __init__(self):
		max_sents = 12
		self.say_q = queue.Queue(max_sents) # Holds the text queue

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

		resp = requests.get(uri, text)
		print(resp.url)
		return self

	def _say(self, audio_data):
		# Pop speech from Q, blocks

		# Spawn subprocess of fmmpeg
		p = subprocess.Popen('./bin/ffplay', '-i', stdin=subprocess.PIPE)

		p.communicate(audio_data)
		# Pipes text to ffmpeg
		# When ffmpeg finishes, unblock Q
		return self


def test_say(speaker):
	speaker.say("Hello, my name is Baymax.")
	speaker.say("I activated because you are in pain.")
	speaker.say("I will scan you now.")
	speaker.say("Are you satisfied with your care?")

def main():
	baymax = Speaker()

	baymax.activate()
	# test_say(baymax)

	baymax.poll()
	baymax.deactivate()


if __name__ == "__main__":
	main()
