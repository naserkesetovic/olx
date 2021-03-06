import math
import requests
import json

from urllib.parse import quote

import konfiguracija
import greske
import razno

from artikal import Artikal
from kategorije import Kategorija, Kategorije
from pretraga import SORT_ORDER, SORT_AT, VRSTA, STANJE, Pretraga

class olx(object):
    def __init__(self):
        ''' Default '''
        pass

    def sve_kategorije(self):
        ''' Hvata spisak svih mogućih kategorija, sa podkategorijama '''

        r = requests.get(konfiguracija.url.format('kategorije'))
        r.raise_for_status()

        if r.status_code == 200:
            results = self.__sve_kategorije(r.json().get('kategorije'))
        else:
            raise greske.ServerUnavailableError
            return None

        return Kategorije(results)

    def __sve_kategorije(self, kategorije):
        results = []
        for k in kategorije:
            potkategorije = []
            id = k.get('id')
            naziv = k.get('naziv')

            if k.get('potkategorije') is not None and len(k.get('potkategorije')) > 0:
                potkategorije = self.__sve_kategorije(k.get('potkategorije'))

            results.append(Kategorija(id, naziv, potkategorije))

        return results

    def trazi(self,
        sta,
        sort_order : SORT_ORDER = SORT_ORDER.DESC,
        sort_po : SORT_AT = SORT_AT.DATUM,
        stanje : STANJE = STANJE.SVE,
        vrsta : VRSTA = VRSTA.SVE,
        besplatnadostava = "ne",
        od = 0,
        do = 0,
        stranica = 1):
        q = ("artikli?trazilica={0}"
        "&sort_order={1}"
        "&sort_po={2}"
        "&vrsta={3}"
        "&stanje={4}"
        "&stranica={5}").format(
            quote(sta),
            sort_order.value,
            sort_po.value,
            vrsta.value,
            stanje.value,
            stranica)

        if besplatnadostava == "da":
            q += "&besplatnadostava=besplatnadostava"

        if isinstance(od, int):
            if int(od) >= 0:
                q += "&od={0}".format(od)

        if isinstance(do, int):
            if int(do) >= 0:
                q += "&do={0}".format(do)

        razno.log("String: {0}".format(q))
        r = requests.get(konfiguracija.url.format(q))

        r.raise_for_status()
        # TODO: status kod
        j = r.json()

        articles = self.__artikli(j.get('artikli'))
        ukupno_rezultata = int(j.get('broj_rezultata'))
        ukupno_stranica = razno.ukupno_stranica(j.get('broj_rezultata'), len(j.get('artikli')))

        return Pretraga(q, articles, stranica, ukupno_stranica, ukupno_rezultata)

    def __artikli(self, articles):
        results = []
        for a in articles:
            results.append(Artikal(
                a.get('id'),
                a.get('naslov'),
                a.get('ima_dostavu'),
                a.get('slika'),
                a.get('cijena'),
                a.get('kategorija'),
                a.get('timestamp'),
                a.get('izdvojen'),
                a.get('istakni'),
                a.get('hitno'),
                a.get('novo'),
                a.get('vidljiv'),
                a.get('radnja'),
                a.get('vrsta_prodaje'),
                a.get('kolicina'),
                a.get('prikazi_kolicinu'),
                a.get('podrzava_kolicinu'),
                a.get('besplatna_dostava'),
            ))

        return results
