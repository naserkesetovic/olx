import time
import math
import konfiguracija


def log(poruka):
    if konfiguracija.DEBUG_MODE:
        print("[{0}] {1}".format(time.strftime("%H:%M"), poruka))


def ukupno_stranica(results, articles):
    if int(results) > 0 and int(articles) > 0:
        return math.ceil(int(results) / int(articles))
    else:
        return 1