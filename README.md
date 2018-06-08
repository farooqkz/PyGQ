# PyGQ
### A python module to get Quran verses using GlobalQuran API
## Moved to https://notabug.org/farooqkz/PyGQ

PyGQ uses GlobalQuran API to get Quran verses in multiple translations. It was
a part of KoranFinder after I decided to re-write this part and now it can be
used as an independent module.

## Usage
This is a sample code with PyGQ which gets the first ayah of the first surah:
```python
import pygq
Q = pygq.PyGQ()
print(Q.getAyah(1, 1, "en.sahih")["verse"])
```
You could use it as a command line tool, too:
```
pygq.py surah:ayah [language code]
```
language code is `en.sahih` by default.

_Note that getAyah() returns a dictionary containing the ayah text, number, surah
number and id._

## Licence
see ISC.

