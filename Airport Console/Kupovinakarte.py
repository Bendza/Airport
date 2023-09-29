import flightLines
import kupci
import avioni
import login
from datetime import datetime, timedelta
karte = []

def nadjiId():
    id = 0

    for karta in karte:
        if int(karta['id']) > id:
            id = int(karta['id'])

    return id + 1

def kupovinaKarte(prodavac):
    print('Kupovina')
    flightLines.formatflights(flightLines.flights)

    let = None

    while let == None:
        brojLeta = input('Broj leta --> ')
        let = flightLines.search('brojLeta', brojLeta)

    kupac = None

    while kupac == None:
        brojpasosa = input('Broj pasosa --> ')
        kupac = kupci.searchkupci('brojpasosa', brojpasosa)

    avion = avioni.searchavioni('naziv', let['modelaviona'])

    brojredova = input('Unesite broj reda --> ')
    brojsedista = input('Unesite broj sedista --> ')
    while int(brojredova) > int(avion['brojredova']):
         print('Na avionu ne postoji toliko redova')

    while int(brojsedista) > int(avion['brojsedista']):
         print('Na avionu ne postoji toliko sedista')


    user = None
    flight = None

    datumprodaje = datetime.now().strftime('%d.%m.%Y')
    karta = {}
    karta['id'] = nadjiId()
    karta['let'] = let['brojLeta']
    karta['kupac'] = kupac['ime']
    karta['pasos'] = kupac['brojpasosa']
    karta['red'] = brojredova
    karta['sediste'] = brojsedista
    karta['datump'] = let['datump']
    karta['datums'] = let['datums']
    karta['datumprodaje'] = datumprodaje
    karta['prodavac'] = prodavac['ime']
    karta['cena'] = let['cena']
    karte.append(karta)
    savekarta()
    print('Karta uspesno rezervisana!')

def loadkarte():
    for line in open('karte.txt','r').readlines():
        if len(line) > 1:
            karta=str2karta(line)
            karte.append(karta)

def str2karta(line):
    if line[-1] == '\n':
        line = line[:-1]
    id, let, kupac, pasos, red, sediste, datump , datums, prodavac, datumprodaje, cena= line.split('|')
    karta = {
      'id': id,
      'let': let,
      'kupac': kupac,
      'pasos': pasos,
      'red': red,
      'sediste': sediste,
      'datump': datump,
      'datums': datums,
      'prodavac': prodavac,
      'datumprodaje':datumprodaje,
      'cena':cena
    }
    return karta

def karte2str(karta):
    return '|'.join([str(karta['id']), karta['let'], karta['kupac'],
                    karta['pasos'], karta['red'], karta['sediste'],
                     karta['datump'], karta['datums'],karta['prodavac'],karta['datumprodaje'],karta['cena']])

def savekarta():
    file = open('karte.txt', 'w')
    for karta in karte:
        file.write(karte2str(karta))
        file.write('\n')
    file.close()

def nadjiKartu(brojLeta, pasos):

    for karta in karte:
        if karta['let'] == brojLeta and karta['pasos'] == pasos:
            return karta

    return None

def izmena():
    brojLeta = input('Unesite broj leta --> ')
    pasos =  input('Unesite broj pasosa putnika --> ')

    karta = nadjiKartu(brojLeta,pasos)

    if karta is None:
        print('Nepostojeca karta')
        return

    print('Izmena karte')

    ime = input('Unesite ime putnika --> ')
    pasos = input('Unesite broj pasosa putnika -->')

    if not proverakupaca(ime, pasos):
        print('Nepostojeci kupac')
        return

    karta['kupac'] = ime
    karta['pasos'] = pasos
    karta['red'] = input('Unesite red --> ')
    karta['sediste'] = input('Unesite sediste --> ')
    karta['datump'] = input('Unesite datum poletanja --> ')
    karta['datums'] = karta['datump']
    savekarta()
    print('Uspesno izmenjena karta!')

def proverakupaca(ime,pasos):
    for kupac in kupci.kupci:
        if ime == kupac['ime'] and pasos == kupac['brojpasosa']:
            return True

    return False


def brisanje():
    brojLeta = input('Unesite broj leta --> ')
    datump = input('Unesite datum poletanja --> ')
    pasos = input('Unesite broj pasosa putnika --> ')

    karta = nadjiKartu(brojLeta, datump, pasos)

    if karta is None:
        print('Nepostojeca karta')
        return

    else: karte.remove(karta)
    savekarta()


def ispisdanprodaje(datumprodaje): #izvestaj1
    print('Ispis karata po danu prodaje')
    datumprodaje = input('Unesite datum u formatu (DD/MM/YYYY) --> ')

    result = []

    for karta in karte:
        if karta['datumprodaje'] == datumprodaje:
            result.append(karta)

    print('\n')
    print(header())
    for karta in karte:
        print(headerkarta(karta))


def ispisdanpolazka(datumpolaska): #izvestaj2
    print('Ispis karata po datumu polaska')
    datumpolaska = input('Unesite datum u formatu (DD/MM) --> ')

    result = []

    for karta in karte:
        if karta['datump'] == datumpolaska:
            result.append(karta)
    print('\n')
    print(header())
    for karta in karte:
        print(headerkarta(karta))

def ispisdaniprodavac(): #izvestaj3
    print('Ispis karata po datumu polaska i prodavcu')
    datumpolaska = input('Unesite datum u formatu (DD/MM) --> ')
    prodavac = input('Unesite ime --> ')

    result= []

    for karta in karte:
        if karta['datump'] == datumpolaska and karta['prodavac'] == prodavac:
            result.append(karta)

    print('\n')
    print(header())
    for karta in result:
        print(headerkarta(karta))

def ispiscena(): #izvestaj4
    datumprodaje = input('Unesite datum u formatu (DD/MM/YYYY):')

    suma = 0
    brojac = 0

    for karta in karte:
        if karta['datumprodaje'] == datumprodaje:
            let = flightLines.findlet(karta['let'])

            suma = suma + int(let['cena'])
            brojac = brojac + 1

    print('\n')
    print(header1())
    print(headerkarta1(suma, brojac))

def ispiscenadatum(datump): #izvestaj5
    datump = input('Unesite datum u formatu (DD/MM)')

    suma = 0
    brojac = 0

    for karta in karte:
        if karta['datump'] == datump:
            let = flightLines.findlet(karta['let'])

            suma = suma + int(let['cena'])
            brojac = brojac + 1

    print('\n')
    print(header1())
    print(headerkarta1(suma, brojac))

def ispiscenadatumiprodavac(): #izvestaj6
    datump = input('Unesite datum u formatu (DD/MM)')
    prodavac = input ('Unesite prodavca ')

    suma = 0
    brojac = 0

    for karta in karte:
        if karta['datump'] == datump and karta['prodavac'] == prodavac:
            let = flightLines.findlet(karta['let'])

            suma = suma + int(let['cena'])
            brojac = brojac + 1

    print('\n')
    print(header1())
    print(headerkarta1(suma, brojac))

def ispisprodavci(): #izvestaj7

    for prodavac in login.users:
        if prodavac['radnomesto'] == 'Menadzer':
            continue
        print(prodavac['ime'])
        suma = 0
        brojac = 0
        for karta in karte:
            datum = datetime.now() - timedelta(days=30)
            kartadatum = datetime.strptime(karta['datumprodaje'], '%d.%m.%Y')

            if prodavac['ime'] == karta['prodavac'] and kartadatum >= datum:
                let = flightLines.findlet(karta['let'])

                suma= suma + int(let['cena'])
                brojac = brojac + 1

        print('\n')
        print(header2())
        print(headerkarta2(suma, brojac,prodavac))


def header():
    return "Broj Leta  |Kupac     |Broj pasosa |Red |Sediste |Datum poletanja  |Datum sletanja  |Prodavac  |Datum prodaje |Cena  |\n" \
           "-----------+----------+------------+----+--------+-----------------+----------------+----------+--------------+------+\n"

def headerkarta(karta):
    return "{0:11}|{1:10}|{2:12}|{3:4}|{4:8}|{5:17}|{6:17}{7:12}{8:13}|{9:5}".format(
      karta['let'],
      karta['kupac'],
      karta['pasos'],
      karta['red'],
      karta['sediste'],
      karta['datump'],
      karta['datums'],
      karta['prodavac'],
      karta['datumprodaje'],
      karta['cena']
    )

def formatkarte(karta):
    result = ''
    for karta in karte:
        result = formatkarte(karta) + '\n'
    return result

def header1():
    return  'Ukupan broj karti | Ukupna cena karti|\n'\
            '------------------+------------------+\n'
def headerkarta1(suma,brojac):
    return '{0:18}|{1:18}'.format(
        brojac,
        suma
    )

def formatkarte1(karta):
    result = ''
    for karta in karte:
        result = formatkarte1(karta) + '\n'
    return result

def header2():
    return 'Ukupan broj karti | Ukupna cena karti|Prodavac        \n' \
           '------------------+------------------+---------------+\n'

def headerkarta2(suma,brojac,prodavac):
    return '{0:18}|{1:18}{2:15}'.format(
        brojac,
        suma,
        prodavac['ime']
    )

def formatkarte2(karta):
    result =''
    for karta in karte:
        result = formatkarte2(karta) +'\n'

    return result


