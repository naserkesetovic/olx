import konfiguracija
import greske
import razno

class Kategorija(object):
    ''' OLX kategorija '''
    def __init__(self, id, naziv, potkategorije):
        self.id = id
        self.naziv = naziv
        self.potkategorije = potkategorije
    
    def __len__(self):
        return len(self.potkategorije)


class Kategorije(object):
    def __init__(self, kategorije):
        self.kategorije = kategorije

    def __len__(self):
        return len(self.kategorije)

    def trazi(self, q):
        results = []

        if q is None:
            raise greske.UndefinedError
            return None

        for k in self.kategorije:
            if q in k.naziv.lower():
                results.append(k)

            if k.potkategorije is not None and len(k.potkategorije) > 0:
                r = self.__trazi(k.potkategorije, q.lower())
                if len(r) > 0:
                    results += r

        return results

    def __trazi(self, potkategorije, q):
        results = []
        for pk in potkategorije:
            if q in pk.naziv.lower():
                razno.log("Pronađeno: {0}".format(pk.naziv))
                results.append(pk)

            if pk.potkategorije is not None and len(pk.potkategorije) > 0:
                r = self.__trazi(pk.potkategorije, q)
                if len(r) > 0:
                    results += r

        return results