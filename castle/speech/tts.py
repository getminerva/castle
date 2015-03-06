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

# import some audio module or cmd whatever
import subprocess

# Use some TTS service before I roll my own
import requests # to make API call

import queue # to hold texts to say
import thread # to make things happen at the same time

# Process
# import numpy # to do necessary numerical computations
class Player(object):

	raise NotImplementedError

class Speaker(object):
	"""
	Speaker object.
	"""

	def __init__(self):
		max_sents = 12

		# Queue to represent what texts have not been said, what texts have been said, and what texts are being said.
		self.unsaid = queue.Queue()
		self.saying = ''
		self.said = []

		self.paused = False

	def say(self, text):
		"""
		Takes text and speaks it.

		Puts it through a pre-processor and (temporarily) hits the TTS API with it.
		"""
		uri = "http://tts-api.com/tts.mp3"

		resp = requests.get(uri, text)
		print(resp.url)
		return self

	def say_now(self, text):
		raise NotImplementedError

	def interject(self, text):
		raise NotImplementedError

	def _say(self, text):
		# Pop speech from Q, blocks

		# Spawn subprocess of fmmpeg
		p = subprocess.Popen(['./bin/ffplay', '-nodisp', '-autoexit', '-i', audio_link])
		# When ffmpeg finishes, unblock Q
		return self

	def activate(self):
		"""
		Primes self to output whatever is in the self.unsaid.

		Spawns a player controlling responsible for outputting the sound. The player is responsible for contnuously checking the 'playlist' (text queue) and this is the controller/liason between that and self.
		"""
		raise NotImplementedError

	def deactivate(self):
		"""
		Kills the thread responsible for outputting the speech.
		"""
		raise NotImplementedError


def test_say(speaker):
	# These commands should execute but produce no simultaneous output. What should happen is that text should be spoken  in the order it was added to the speaker queue (called)
	speaker.say("Hello, I am Baymax, your personal healthcare companion.")
	speaker.say("On a scale of one to ten, how would you rate your injuries?")
	speaker.say("I will scan you for injuries.")
	speaker.say("Scan complete.")
	speaker.say("It is okay to cry. Crying is a natural response to pain.")
	speaker.say("Are you satisfied with your care?")

def test_say_now(speaker):
	# Should execute and speak immediately (or right after it finishes saying something)
	speaker.say_now("Scan complete.")

def test_interject(speaker):
	# Should execute and pause any current output, executing immediately.
	speaker.interject("WATCH OUT!")

def main():
	# Initialize speaker
	baymax = Speaker()

	# Activate output mode - prime it to receive input and produce output
	baymax.activate()

	# Testing
	test_say(baymax)
	test_say_now(baymax)
	test_interject(baymax)

	# Deactivate output mode, can still receive input but will not speak.
	baymax.deactivate()

if __name__ == "__main__":
	main()
