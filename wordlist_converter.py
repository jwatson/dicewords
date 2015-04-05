# vim: set fileencoding=utf-8


import json
import re
import sys


def read_wordlist(file):
    with open(file) as f:
        data = f.readlines()

    return data


def make_dicedict(dicewords):
    regex = re.compile(r"(\d\d\d\d\d)\s+(\w+)")
    dicedict = {}
    for line in dicewords:
        match = regex.match(line)
        if match is not None:
            (key, value) = match.group(1), match.group(2)
            dicedict[key] = value

    return dicedict


def write_jsonfile(file, dicedict):
    with open(sys.argv[2], 'w') as f:
        json.dump(dicedict, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <wordlist> <jsonfile>".format(sys.argv[0]))
        sys.exit(-1)

    dicewords = read_wordlist(sys.argv[1])
    dicedict = make_dicedict(dicewords)
    write_jsonfile(sys.argv[2], dicedict)
