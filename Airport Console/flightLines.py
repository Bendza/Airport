kupci=[]
flights=[]


def loadflights():
    for line in open('flights.txt','r').readlines():
        if len(line) > 1:
            flight =str2flight(line)
            flights.append(flight)

def flight2str(flight):
    return '|'.join([flight['brojleta'],flight['polaziste'],flight['odrediste'],
                    flight['vremep'],flight['vremes'],flight['kompanija'],
                    flight['datump'],flight['datums'],flight['modelaviona'],flight['cena']])

def str2flight(line):
    if line[-1] == '\n':
        line = line[:-1]
        brojleta,polaziste,odrediste,vremep,vremes,kompanija,datump,datums,modelaviona,cena=line.strip('\n').split('|')
        flight ={
        'brojLeta':brojleta,
        'polaziste':polaziste,
        'odrediste':odrediste,
        'vremep':vremep,
        'vremes':vremes,
        'kompanija':kompanija,
        'datump':datump,
        'datums':datums,
        'modelaviona':modelaviona,
        'cena':cena,
        }
        return flight

def search(field, value):
    for flight in flights:
        if flight[field].upper() == value.upper():
            return flight
    return None

def searchflightLines(field, value):
    result = []
    for flight in flights:
        if flight[field].upper() == value.upper():
            result.append(flight)
    return result

def formatheader():
    return "Broj Leta  |Polaziste |Odrediste |Vreme poletanja |Vreme sletanja |Kompanija    |Datum poletanja  |Datum Sletanja  |Model aviona | Cena |    \n" \
           "-----------+----------+----------+----------------+---------------+-------------+-----------------+----------------+-------------+------+\n"

def formatflight(flight):
    return u"{0:11}|{1:10}|{2:10}|{3:16}|{4:15}|{5:13}|{6:17}{7:16}{8:13}|{9:7}".format(
      flight['brojLeta'],
      flight['polaziste'],
      flight['odrediste'],
      flight['vremep'],
      flight['vremes'],
      flight['kompanija'],
      flight['datump'],
      flight['datums'],
      flight['modelaviona'],
      flight['cena']
    )


def formatflights(flights):
    result = ''
    for flight in flights:
        result = formatflight(flight) + '\n'
    return result


def findlet(brojLeta):
    for let in flights:
        if let['brojLeta'] == brojLeta:
            return let

    return None






