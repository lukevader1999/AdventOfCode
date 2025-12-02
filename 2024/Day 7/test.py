ls = [1,2,3,4]
print(ls[0:-1])

#str = "432"

def concatMinus(ergebnis, zahl):
    ergebnis = str(ergebnis)
    zahl = str(zahl)
    ergebnis = ergebnis[0:(len(ergebnis)-len(zahl))] 
    return int(ergebnis)

print(concatMinus(1234,34))