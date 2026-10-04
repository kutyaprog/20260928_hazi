import random
import math

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

szel = float(input("szelesseg: "))
hossz = float(input("hosszusag: "))
ado = float(input("Ado: "))
if szel <= 15 and hossz <= 25:
    ado = ado*0.8
    print(ado)

# 29 feladat
t = int(input("evszam: "))
a = t % 19
b = t % 4
c = t % 7
d = (19*a + 24) % 30
e = (2*b+4*c+6*d+5) % 7
h = 22 + d + e
if e == 6 and d == 29:
    h = 50
elif e == 6 and d == 28 and a > 10:
    h = 49
if h <= 31:
    print(f"marcius {h}")
else:
    print(f"paril {h-31}")


#30
jegy = int(input("Jegy: "))
if jegy == 1:
    print("Elégtelen")
elif jegy == 2:
    print("Elegseges")
elif jegy == 3:
    print("Kozepes")
elif jegy == 4:
    print("Jo")
elif jegy == 5:
    print("Jeles")
else:
    print("Ervénytelen erdemjegy")

#31

nap = int(input("A het hányadik napja: "))
if nap == 1:
    print("Hetfo")
elif nap == 2:
    print("Kedd")
elif nap == 3:
    print("Szerda")
elif nap == 4:
    print("Csutortok")
elif nap == 5:
    print("Pentek")
elif nap == 6:
    print("Szombat")
else:
    print("Vasarnap")


#32
ev = int(input("Ev: "))
honap = int(input("Honap: "))
nap = int(input("Nap: "))

if honap == 1:
    honapsz = "januar"
elif honap == 2:
    honapsz = "februar"
elif honap == 3:
    honapsz = "marcius"
elif honap == 4:
    honapsz = "aprilis"
elif honap == 5:
    honapsz = "majus"
elif honap == 6:
    honapsz = "junius"
elif honap == 7:
    honapsz = "julius"
elif honap == 8:
    honapsz = "augusztus"
elif honap == 9:
    honapsz = "szeptember"
elif honap == 10:
    honapsz = "oktober"
elif honap == 11:
    honapsz = "november"
else:
    honapsz = "december"

print(f"{ev} {honapsz} {nap}")

#33
dobas = random.randint(1, 6)
print(f"Dobas: {dobas}")
if dobas <= 2:
    print("Gyenge!")
elif dobas <= 4:
    print("Nem rossz!")
elif dobas == 5:
    print("Jo!")
else:
    print("Kivalo!")



#34

print("a", random.randint(0, 100))
print("b", random.randint(-100, 0))
print("c", random.randint(10, 90))
print("d", random.randint(-100, 100))
print("e", random.randint(-50, 50))
print("f", random.randint(1000, 2000))
print("g", random.randint(8000, 150000))

#35
lab = float(input("Lab: "))
huvely = float(input("Huvelyk: "))
cm = (lab * 30.48) + (huvely * 2.54)
print(f"{cm} cm")

#36 
gallon = float(input("Gallon viz: "))
liter = gallon * 4.543
tomegkg = liter * 0.998
tomegdkg = tomegkg * 100
font = tomegdkg / 45.36
print(f"{font} font")

#37

nap = int(input("Honap hanyadik napja: "))
ora = int(input("Hány ora (0-23): "))
osszes_ora = (nap - 1) * 24 + ora
print(f"A honap {osszes_ora}. oraja")

print("38f")
degrees = int(input("Szögmérték: "))
rad = math.radians(degrees)
print(f"{rad} radián")

# 39
print("39f")
szamAbs = abs(float(input("Valós szám: ")))
print(f"Az abs érték {szamAbs}")

# 40
bin_szam = input("5 szamot: ")
tizes = int(bin_szam[0]) * 8 + int(bin_szam[1]) * 4 + int(bin_szam[2]) * 2 + int(bin_szam[3]) * 1
print(f"10-es: {tizes}")





a = float(input("a befogo: "))
b = float(input("b befogo: "))
c = (a**2 + b**2) ** 0.5
print(f"Atfogo: {c}")