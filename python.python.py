import random

#21
pont = int(input("Hány pont? "))

if pont < 42: 
    print("Elégtelen")
elif pont < 57:
    print("Elégséges")
elif pont < 72:
    print("közepes")
elif pont < 87:
    print("jó")
else:
    print("jeles")

#22

ev = int(input("Életkor: "))

if ev < 13:
    print("Gyerek")
elif ev < 17:
    print("Fiatalkorú")
elif ev < 23:
    print("Ifjú")
elif ev < 59:
    print("Fenlőtt")
else:
    print("Idős")

#23

fsuruseg = float(input("folyadék sűrűsége"))
tsuruseg = float(input("Tárgy sűrűsége"))

if tsuruseg < fsuruseg:
    print("Lebeg a tárgy")
elif tsuruseg == fsuruseg:
    print("a tárgy úszik")
else:
    print(" a tárgy elmerűl")

#24

hianyzas = int(input("Diák igazolatlan hiányzásai: "))
if hianyzas == 0:
    print("5")
elif hianyzas <= 3:
    print("4")
elif hianyzas <= 9:
    print("3")
elif hianyzas > 10:
    ev = int(input("Hány éves: "))
    if ev < 18:
        print("szülői értesítés szükséges")
    else:
        print("Felszólítás szükséges")

#25

karakter = input("Írjon egy karaktert")
aszki = ord(karakter)
if aszki >= 48 or aszki <= 57:
    print("szamok")
elif aszki >= 65 or aszki <=90:
    print("nagy angol abc")
elif aszki >=97 or aszki <=122:
    print("kis angol abc")
else:
    print("egyeb")

#26

seb = int(input("Iadja meg a sebességét KM/Hbna"))

if seb <= 1:
    print("csiga")
elif seb <=6:
    print("csuka")
elif seb <=32:
    print("bálna")
elif seb <=48:
    print("ezüst sirály")
elif seb <=64:
    print("nyúl")
elif seb <=70:
    print("strucc")
elif seb <=110:
    print("gepárd")
elif seb <=320:
    print("vadászsólyom")

#27

tav = float(input("Mekkora volt a táv? "))
if tav <=2:
    print("500Ft")
elif tav <= 5:
    print("700Ft")
elif tav <= 10:
    print("900 Ft")
elif tav <= 20:
    print("1400Ft")
elif tav <=30:
    print("2000Ft")

#28







