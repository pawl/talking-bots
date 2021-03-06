import urllib2
import urllib
import time
import os
import sys


def speak(text='hello', lang='en', fname='result.wav', player='mplayer'):
    """ Send text to Google's text to speech service
    and returns created speech (wav file). """

    limit = min(100, len(text))#100 characters is the current limit.
    text = text[0:limit]
    url = "http://translate.google.com/translate_tts"
    values = urllib.urlencode({"q": text, "textlen": len(text), "tl": lang})
    hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}
    #TODO catch exceptions
    req = urllib2.Request(url, data=values, headers=hrs)
    p = urllib2.urlopen(req)
    f = open(fname, 'wb')
    f.write(p.read())
    f.close()
    play_wav(fname, player)


def play_wav(filep, player='mplayer'):
    os.system(player + " " + filep + ">/dev/null")


if(__name__ == '__main__'):
    speak(sys.argv[1],sys.argv[2])
