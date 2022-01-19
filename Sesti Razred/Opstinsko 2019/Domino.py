Domino1 = str(input())
Domino2 = str(input())
Domino1c = []
Domino2c = []
Domino1c.append(int(Domino1.split(" ")[0]))
Domino1c.append(int(Domino1.split(" ")[1]))

Domino2c.append(int(Domino2.split(" ")[0]))
Domino2c.append(int(Domino2.split(" ")[1]))


Kombinacija = ""

ObeL = Domino2c + Domino1c
NajvecaCifra1 = max(Domino1c)
NajmanjaCifra1 = min(Domino1c)
NajvecaCifra2 = max(Domino2c)
NajmanjaCifra2 = min(Domino2c)
veci = 0


if NajvecaCifra1 < NajvecaCifra2:
    veci = 2
elif NajvecaCifra2 == NajvecaCifra1:
    if NajmanjaCifra1 > NajmanjaCifra2:
        veci = 1
    elif NajmanjaCifra2 > NajmanjaCifra1:
        veci = 2
    else:
        veci = -2
elif NajvecaCifra1 > NajvecaCifra2:
    veci = 1

if veci == -1:
    Kombinacija = (
        Kombinacija
        + str(Domino1c[0])
        + str(Domino1c[1])
        + str(Domino2c[0])
        + str(Domino2c[1])
    )
if veci == 1:
    Kombinacija = (
        Kombinacija
        + str(NajvecaCifra1)
        + str(NajmanjaCifra1)
        + str(NajvecaCifra2)
        + str(NajmanjaCifra2)
    )
if veci == 2:
    Kombinacija = (
        Kombinacija
        + str(NajvecaCifra2)
        + str(NajmanjaCifra2)
        + str(NajvecaCifra1)
        + str(NajmanjaCifra1)
    )
if veci == -2:
    Kombinacija = (
        Kombinacija
        + str(NajvecaCifra1)
        + str(NajmanjaCifra1)
        + str(NajvecaCifra2)
        + str(NajmanjaCifra2)
    )


NajvecaCifra = max(Domino1c[0], Domino1c[1], Domino2c[0], Domino2c[1])
print(NajvecaCifra)
prvaCifra = NajvecaCifra
print(Kombinacija)
