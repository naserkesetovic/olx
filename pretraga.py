import enum

class SORT_ORDER(enum.Enum):
    DESC = "desc"
    ASC = "asc"

class SORT_AT(enum.Enum):
    DATUM = "datum"

class STANJE(enum.Enum):
    SVE = 0
    NOVO = 1
    KORISTENO = 2

class VRSTA(enum.Enum):
    SAMOPRODAJA = "samoprodaja"
    SAMOIZDAVANJE = "samoizdavanje"
    SAMOPOTRAZNJA = "samopotraznja"
    SVE = ""

class Pretraga(object):
    def __init__(self, trazeno, artikli, stranica, ukupno_stranica, ukupno_rezultata):
        self.trazeno = trazeno
        self.artikli = artikli
        self.stranica = stranica
        self.ukupno_stranica = ukupno_stranica
        self.ukupno_rezultata = ukupno_rezultata


    def __len__(self):
        return len(self.artikli)
