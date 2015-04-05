# Diceware • A Secure Diceware-based Passphrase Generator

[Diceware](http://world.std.com/~reinhold/diceware.html) is a mechanism for
creating strong, easy to remember passphrases.

I think my `urandom` + `SHA-256` + `Mersenne Twister` approach to randomness
makes sense, but anything security related is best viewed by peers.

## Usage

For now, you'll have to clone the repo. If there's interest, I'll upload it to
[pypi](https://pypi.python.org/pypi) and make it
[pipsi](https://github.com/mitsuhiko/pipsi)-friendly.

```sh
$ git clone https://github.com/jwatson/diceware.git
$ cd diceware
$ curl -O http://world.std.com/%7Ereinhold/diceware.wordlist.asc
$ python wordlist_converter.py diceware.wordlist.asc dicewords.json
$ python dicegen.py dicewords.json 7 10
```
