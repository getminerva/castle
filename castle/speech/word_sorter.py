#!/usr/bin/python

def feed_words(sentence):
    for token in sentence.split():
        yield token

class Tagger(object):

    def __init__(self):
        self.curword = None
        self.curraw = []

    def tag(self, word):
        tag = "NN"
        return (word, tag)

    def get_last_word(self):
        return self.curraw[-1] or None

    def get_raw(self):
        return self.curraw


class Token_Sorter(object):

    def __init__(self):
        pass

    def assign(self, cmd, token):
        # This is where the magic actually happens - maybe?
        pass

def main():
    vcmd = "Can you please turn the lights off."

    raw = []
    cmd = {'dev':None, 'feat':None, 'val':None}
    for word in feed_words(cmd_lights):
        # Bag
        raw.append(word)
        print("Current: {}".format(word))
        print("Raw: {}".format(raw))
        # Tag (or hold if part of phrase)
        # token = tagger.tag(word)

        # Now i have to somehow figure out how to sort the word/phrase using the pos into a piece of th cmd
        # token_sorter.assign(cmd, token)

if __name__ == "__main__":
    main()
