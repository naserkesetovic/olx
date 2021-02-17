DEBUG_MODE = True
REZULTATA_PO_STRANICI = 30

url = "http://api.pik.ba/{0}"

# https://www.olx.ba/ajax/gradovi?kanton=9
# https://api.pik.ba/artikli?trazilica=mobitel
# https://www.olx.ba/pretraga?trazilica=+mob&kategorija=31&id=3&stanje=1&vrstapregleda=tabela&sort_order=desc
# kategorija = id
# stanje = 0, 1, 2                                      - sve, novo, korišteno
# od = 0                                                - cijena od - prazno ako nema
# do = 20                                               - cijena do - prazno ako nema
# vrsta = samoprodaja, samoizdavanje, samopotraznja,    - posljednja opcija je prazna - sve!
# sacijenom = sacijenom                                 - samo sa cijenom
# filter_slike = 5                                      - sa minimalno 5 slika
# besplatnadostava = besplatnadostava                   - besplatna dostava
# samo_premiumdostava = da                              - olx premium dostava