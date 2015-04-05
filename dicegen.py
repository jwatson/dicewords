# vim: set fileencoding=utf-8


import hashlib
import json
import os
import random
import sys


def randhash():
    """ Generate a hash of random data. """

    # SHA-256 works in multiples of 512 bits, so we'll generate a large
    # number of bytes based on that and then hash them.
    random_bytes = os.urandom((512 * 4) / 8)
    return hashlib.sha256(random_bytes).hexdigest()


def roll_dice():
    """ Simulate the roll of a 6-sided die. """

    pool = randhash()

    # Pick a random byte in the pool to seed our dice roll. It's OK
    # that we're using the Mersenne Twister here, since the source
    # data is reasonably random and obfuscated.
    index = random.SystemRandom().randint(0, len(pool) - 1)
    byte = ord(pool[index])
    return (byte % 6) + 1


def generate_key(n):
    """ Generate a string key of `n` dice rolls. """

    rolls = []
    for x in range(0, n):
        rolls.append(str(roll_dice()))

    return "".join(rolls)


def generate_dicephrase(dicewords_dict, length):
    """ Create a dicewords phrase. """

    words = []
    for x in range(0, length):
        key = generate_key(5)

        while True:
            word = dicewords_dict.get(key)
            if word is not None:
                words.append(word)
                break

    return " ".join(words)


def load_dicefile(file):
    """ Load the dicewords file from disk. """

    with open(file) as f:
        dicewords_dict = json.load(f)

    return dicewords_dict


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <wordfile> <length> <count>".format(sys.argv[0]))
        sys.exit(-1)

    dicewords_dict = load_dicefile(sys.argv[1])

    phrases = []
    for i in range(0, int(sys.argv[3])):
        phrases.append(generate_dicephrase(dicewords_dict, int(sys.argv[2])))

    for p in phrases:
        print p
