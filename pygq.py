"""
Copyright (C) 2018 Farooq Karimi Zadeh <farooghkarimizadeh at gmail dot com>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import requests

class PyGQ:
    SURAH_LAST = 114
    SURAH_FIRST = 1
    def __init__(self, url="http://api.globalquran.com/ayah/", token="", lg_codes={}):
        """url and token are API url and token. lg_codes is a dict which maps 
           2 letter language codes to their fullname. like:
           {"en": "en.sahih", "ar": "quran-simple"}
        """

        self.url = url
        self.token = token
        self.lg_codes = lg_codes

    def getAyah(self, surah, ayah, lang):
        """Returns a dict containing the verse itself, ayah and surah number
        and id. example:
            {
            "surah": 1,
            "ayah": 1,
            "id": 1,
            "verse": "In the name of Allah, the Entirely Merciful, the Especially Merciful."
            }
        """
        if len(lang) == 2:
            if lang in self.lg_codes:
                lang = self.lg_codes[lang]
            else:
                raise ValueError(lang+ " is not supported using 2letter codes")
        
        if (not self.SURAH_FIRST <= surah <= self.SURAH_LAST):
            raise ValueError("surah(chapter) must be between "
                             + str(self.SURAH_FIRST) + " and " +
                             str(self.SURAH_LAST))

        req_url = self.url + str(surah) + ":" + str(ayah) + "/" + lang
        ayah_json = requests.get(req_url, params = {'key': self.token}).json()
        while len(ayah_json) == 1:
            ayah_json = ayah_json[next(iter(ayah_json))]

        if ayah_json["surah"] != surah:
            raise ValueError("Invalid ayah number for this surah")
        
        return ayah_json

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "surah:ayah [lang]")
        sys.exit(0)
    
    surah, ayah = sys.argv[1].split(":")
    surah = int(surah)
    ayah = int(ayah)
    lang = "en.sahih" if len(sys.argv) < 3 else sys.argv[2]

    Q = PyGQ()
    print(Q.getAyah(surah, ayah, lang)["verse"])
    
