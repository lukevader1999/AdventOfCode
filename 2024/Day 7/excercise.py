#Input verarbeiten
input = open("Day 7/input.txt")

def convertLine(line):
    temp = line.split(": ")
    ergebnis = int(temp[0])
    zahlen = [int(x) for x in temp[1].split(" ")]
    return ergebnis, zahlen

rechnungen = []
for line in input:
    rechnungen.append(convertLine(line))

input.close()

#Concat-Possible 
def concatPossible(ergebnis: int, zahl: int) -> bool:
    #Iterate trough string from back to front
    ergebnis = str(ergebnis)
    zahl = str(zahl)
    if len(zahl) > len(ergebnis):
        return False
    for i in range(1,len(zahl)+1):
        if zahl[-i] != ergebnis[-i]:
            return False
    return True

#Concat-Minus Rechnen
#Wirft irgendwann Fehler mit Minuszahlen(am besten vorher abfangen)
def concatMinus(ergebnis: int, zahl:int) -> int:
    ergebnis = str(ergebnis)
    zahl = str(zahl)
    ergebnis = ergebnis[0:len(ergebnis)-len(zahl)] 
    if len(ergebnis) == 0:
        ergebnis = 0
    else:
        ergebnis = int(ergebnis)
    return ergebnis

#Eine Rechnung auf Lösbarkeit prüfen
def rechnungLoesbar(ergebnis, rechnung):
    if len(rechnung) == 1:
        if ergebnis == rechnung[0]:
            return True
        else:
            return False

    if ergebnis < 0:
        return False

    zahl = rechnung[-1]

    if ergebnis % zahl != 0:
        zwischenergebnisMal = False
    else:
        zwischenergebnisMal = rechnungLoesbar(ergebnis//zahl, rechnung[0:-1])

    zwischenergebnisPlus = rechnungLoesbar(ergebnis - zahl, rechnung[0:-1])

    if concatPossible(ergebnis,zahl):
        zwischenergebnisConcat = rechnungLoesbar(concatMinus(ergebnis, zahl),rechnung[0:-1])
    else:
        zwischenergebnisConcat = False

    if zwischenergebnisMal or zwischenergebnisPlus or zwischenergebnisConcat:
        return True
    else:
        return False

res = 0
for rechnung in rechnungen:
    if rechnungLoesbar(rechnung[0],rechnung[1]):
        res += rechnung[0]
print(res)