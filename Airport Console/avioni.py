avioni=[]

def loadavioni():
    for line in open('avioni.txt','r').readlines():
        if len(line) > 1:
            avion=str2avion(line)
            avioni.append(avion)

def avion2str(avion):
    return '|'.join([avion['naziv'], avion['brojredova'], avion['brojsedista']])

def str2avion(line):
    if line[-1] == '\n':
        line = line[:-1]
    naziv,brojredova,brojsedista = line.split('|')
    avion = {
      'naziv': naziv,
      'brojredova': brojredova,
      'brojsedista': brojsedista
    }
    return avion

def formatavioni(avionilista):
    result = ''
    for avion in avioni:
        result = formatavioni(avionilista) + '\n'
    return result

def searchavioni(field,value):
    loadavioni()
    for avion in avioni:
        if avion[field].upper() == value.upper():
            return avion
    return None
