kupci=[]

def loadkupci():
    for line in open('kupci.txt','r').readlines():
        if len(line) > 1:
            kupac=str2kupac(line)
            kupci.append(kupac)

def kupac2str(kupac):
    return '|'.join([kupac['ime'],kupac['prezime'],kupac['drzavljanstvo'],kupac['brojpasosa']])

def str2kupac(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime,prezime,drzavljanstvo,brojpasosa = line.split('|')
    flight = {
      'ime': ime,
      'prezime': prezime,
      'drzavljanstvo': drzavljanstvo,
      'brojpasosa': brojpasosa,
    }
    return flight

def addkupac(kupac):
    kupci.append(kupac)

def savekupci():
    file = open('kupci.txt','w')
    for kupac in kupci:
        file.write(kupac2str(kupac))
        file.write('\n')
    file.close()

def formatkupci(kupcilista):
    result = ''
    for flight in kupcilista:
        result = formatkupci(kupci) + '\n'
    return result

def searchkupci(field,value):
    loadkupci()
    for kupac in kupci:
        if kupac[field].upper() == value.upper():
            return kupac
    return None


