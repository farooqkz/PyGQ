# PyGQ
### A python module to get Quran verses using GlobalQuran API

PyGQ uses GlobalQuran API to get Quran verses in multiple translations. It was
a part of KoranFinder after I decided to re-write this part and now it can be
used as an independent module.

## Usage
This is a sample code with PyGQ which gets the first ayah of the first surah:
```
import pygq
Q = pygq.PyGQ()
print(Q.getAyah(1, 1, "en.sahih")["verse"])
```

_Note that getAyah() returns a Dict containing the ayah text, number, surah
number and id._

## Licence
see ISC.

