class Artikal(object):
    ''' OLX definisani artikal, s dodatnim poljima poput parsirane cijene, timestampa '''
    def __init__(self, id, naslov, ima_dostavu, slika, cijena, kategorija, timestamp, izdvojen, istakni, hitno, novo, vidljiv, radnja, vrsta_prodaje, kolicina, prikazi_kolicinu, podrzava_kolicinu, besplatna_dostava):
        self.id = id
        self.naslov = naslov
        self.ima_dostavu = self.__parse_boolean(ima_dostavu)
        self.slika = slika
        self.slika_thumb = "{0}-thumb.jpg".format(slika)
        self.slika_default = "{0}-default.jpg".format(slika)
        self.cijena = cijena
        self.cijena_int = self.__parse_price(cijena)
        self.kategorija = kategorija
        self.timestamp = timestamp
        self.izdvojen = izdvojen
        self.istakni = self.__parse_boolean(istakni)
        self.hitno = self.__parse_boolean(hitno)
        self.novo = self.__parse_boolean(novo)
        self.vidljiv = self.__parse_boolean(vidljiv)
        self.radnja = self.__parse_boolean(radnja)
        self.vrsta_prodaje = vrsta_prodaje
        self.kolicina = kolicina
        self.prikazi_kolicinu = self.__parse_boolean(prikazi_kolicinu)
        self.podrzava_kolicinu = self.__parse_boolean(podrzava_kolicinu)
        self.besplatna_dostava = self.__parse_boolean(besplatna_dostava)

    @staticmethod
    def __parse_price(cijena):
        try:
            return float(cijena.split(' ')[0])
        except:
            return 0

    @staticmethod
    def __parse_boolean(b):
        if str(b).lower() == 'true' or int(b) == 1:
            return True
        else:
            return False
