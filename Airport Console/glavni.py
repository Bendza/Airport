import login
import flightLines
import kupci
import avioni
import Kupovinakarte
import datetime
import calendar

user = None

def main():
    print ()
    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print ('^          Aerodrom            ^')
    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print()
    flightLines.loadflights()
    Kupovinakarte.loadkarte()
    loging()


def loging():
    users=login.loadusers()
 
    username = input('Username: ')
    password = input('Password: ')

    if login.login(username,password,users) == False:
        print ('Uneli ste nepostojeci username i lozinku!')
        login()
    else:
        user=login.login(username,password,users)
        print('\nUlogovani ste kao' + user['ime'] + ' ' + user['prezime'] + '\n')
        if user['radnomesto'] =='Prodavac':
            menu1(user)
        else:
            menu2()

def printmenu1():
    print('\nIzaberite zeljenu opciju: ')
    print('1 - Pretraga letova')
    print('2 - Unos novih karata')
    print('3 - Izmena postojecih karata')
    print('4 - Brisanje postojecih karata')
    print('0 - Izlaz')

def menu1():
    printmenu1()
    com=' '
    while com != '0':
        printmenu1()
        command = input('--> ')
        com=command.upper()
        if com == '1':
            search()
        elif com == '2':
            Kupovinakarte.kupovinaKarte()
        elif com == '3':
            Kupovinakarte.izmena()
        elif com == '4':
            Kupovinakarte.brisanje()
        elif com == '0':
            return
        else:
            print('\nUneli ste pogresnu komandu')
            printmenu1()

def printmenu2():
    print("\n Izaberite zeljenu opciju: ")
    print(" 1 - Pretraga letova")
    print(" 2 - Izvestaji o prodatim kartama")
    print(" 0 - Izlaz iz programa")


def menu2():
    printmenu2()
    com = ' '
    while com != '0':
        command = input(">> ")
        com = command.upper()
        if com == '1':
            search()
        elif com == '2':
            menuizvestaji(kupci)
        elif com == '0':
            print("Dovidjenja!")
            return
        else:
            print("\nUneli ste pogresnu komandu.\n")





def printmenuizvestaji():
    print('\nIzaberite zeljenu opciju: ')
    print('1 - Izvestaj po danu prodaje')
    print('2 - Izvestaj po danu polazka')
    print('3 - Izvestaj po danu prodaje i prodavcu')
    print('4 - Izvestaj ukupnog broja i cena karti po datumu prodaje')
    print('5 - Izvestaj ukupnog broja i cena karti po datumu poletanja')
    print('6 - Izvestaj ukupnog broja i cena karti po datumu poletanja i prodavcu ')
    print('7 - Izvestaj ukupnog broja i cena karti u poslednjih 30 dana po prodavcu')
    print('0 - Nazad')

def menuizvestaji(prodavac):
    printmenuizvestaji()
    com=' '
    while com !='x':
        command = input ('>> ')
        com=command.upper()
        if com == '1':
            Kupovinakarte.ispisdanprodaje(prodavac)
        elif com == '2':
            Kupovinakarte.ispisdanpolazka(prodavac)
        elif com == '3':
            Kupovinakarte.ispisdaniprodavac()
        elif com == '4':
            Kupovinakarte.ispiscena()
        elif com == '5':
            Kupovinakarte.ispiscenadatum(prodavac)
        elif com == '6':
            Kupovinakarte.ispiscenadatumiprodavac()
        elif com == '7':
            Kupovinakarte.ispisprodavci()
        elif com == '0':
            print('Dovidjenja')
            return
        else:
            print('\nUneli ste pogresnu komandu')
            printmenuizvestaji()

def printsearch():
    print("\n Izaberite zeljenu opciju: ")
    print(" 1 - Pretraga po polazistu")
    print(" 2 - Pretraga po odredistu")
    print(" 3 - Pretraga po vremenu poletanja")
    print(" 4 - Pretraga po vremenu sletanja")
    print(" 5 - Pretraga po datumu poletanja")
    print(' 6 - Pretraga po datumu sletanja')
    print(" 7 - Pretraga po kompaniji")
    print(" 0 - Nazad")

def search():
    printsearch()
    com = ' '
    while com != 'X':
        commanda = input(">> ")
        com = commanda.upper()
        if com == '1':
            searchpolaziste()
        elif com == '2':
            searchodrediste()
        elif com == '3':
            searchvremep()
        elif com == '4':
            searchvremes()
        elif com == '5':
            sreachdatump()
        elif com == '6':
            sreachdatums()
        elif com == '7':
            searchkompanija()
        elif com == '0':
            print('Dovidjenja!')
            menu2()
        else:
            print('Uneli ste pogresnu komandu')
            printsearch()



def searchpolaziste():
    print ("[1] Pretrazianje letova po polazistu\n")

    for item in flightLines.flights:
      print (" -> ",item['polaziste'])  

    polaziste = input("Unesite polaziste >> ")
    flightlist = flightLines.searchflightLines('polaziste', polaziste)
    if len(flightlist) == 0:
        print ("\3nNema trazenih letova.")
    else:
        print ('\n')
        print (flightLines.formatheader())
        print (flightLines.formatflights(flightlist))
        search()

def searchodrediste():
    print ("[2] Pretrazianje letova po odredistu\n")
    for item in flightLines.flights:
      print (" -> ",item['odrediste'])
    odrediste = input("Unesite odrediste >> ")
    flightList = flightLines.searchflightLines('odrediste', odrediste)
    if len(flightList) == 0:
        print ("\nNema trazenih letova.")
    else:
        print ('\n')
        print (flightLines.formatheader())
        print (flightLines.formatflights(flightList))
        search()

def searchvremep():
    print ("[3] Pretrazianje letova po vremenu poletanja\n")
    for item in flightLines.flights:
        print(" -> ", item['vremep'])
    vremep = input("Unesite vreme poletanja >> ")
    flightList = flightLines.searchflightLines('vremep', vremep)
    if len(flightList) == 0:
        print ("\nNema trazenih letova.")
    else:
        print ('\n')
        print (flightLines.formatheader())
        print (flightLines.formatflights(flightList))
        search()

def searchvremes():
    print ("[4] Pretrazianje letova po vremenu sletanja\n")
    for item in flightLines.flights:
        print("-->",item['vremes'])
    vremes = input("Unesite vreme sletanja >> ")
    flightList = flightLines.searchflightLines('vremes', vremes)
    if len(flightList) == 0:
        print ("\nNema trazenih letova.")
    else:
        print ('\n')
        print (flightLines.formatheader())
        print (flightLines.formatflights(flightList))
        search()


def sreachdatump():
    print('[5] Pretrazivanje letova po datumu poletanja\n')
    for item in flightLines.flights:
        print('-->',item['datump'])
    datump = input('Unesite zeljeni datum poletanja')
    flightList = flightLines.searchflightLines('datump',datump)
    if len(flightList) == 0:
        print("\nNema trazenih letova.")
    else:
        print('\n')
        print(flightLines.formatheader())
        print(flightLines.formatflights(flightList))
        search()

def sreachdatums():
    print('[6] Pretrazivanje letova po datumu sletanja\n')
    for item in flightLines.flights:
        print('-->',item['datums'])
    datums = input('Unesite zeljeni datum sletanja')
    flightList = flightLines.searchflightLines('datums', datums)
    if len(flightList) == 0:
        print("\nNema trazenih letova.")
    else:
        print('\n')
        print(flightLines.formatheader())
        print(flightLines.formatflights(flightList))
        search()



def searchkompanija():
    print ("[7] Pretrazianje letova po kompaniji\n")
    for item in flightLines.flights:
        print("-->", item['kompanija'])
    kompanija = input("Unesite zeljenu kompaniju >> ")
    flightList = flightLines.searchflightLines('kompanija', kompanija)
    if len(flightList) == 0:
        print ("\nNema trazenih letova.")
    else:
        print ('\n')
        print (flightLines.formatheader())
        print (flightLines.formatflights(flightList))
        search()



if __name__ == '__main__':
  main()
