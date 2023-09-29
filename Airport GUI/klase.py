class let:
    def __init__(self,id,mestop,mestos,cena,):
        self.id = id
        self.mestopolaska = mestop
        self.mestodolazka = mestos
        self.cena = cena

    def __str__(self):
        return f'{self.id} | {self.mestopolaska} | {self.mestodolazka} | {self.cena}'


class user:
    def __init__(self,username,password,radnomesto):
        self.username = username
        self.password = password
        self.radnomesto = radnomesto

    def __str__(self):
        return f'{self.username} | {self.password} | {self.radnomesto}'


class karta:
    def __init__(self,id,idleta,ime,prezime,prodavac,cena):
        self.id = id
        self.idleta = idleta
        self.ime = ime
        self.prezime = prezime
        self.prodavac = prodavac
        self.cena = cena

    def __str__(self):
        return f'{self.id} | {self.idleta} | {self.ime} | {self.prezime} | {self.prodavac} | {self.cena}'
