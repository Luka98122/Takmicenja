Cifre = str(input())
PrviDomino = str(Cifre.split(" ")[0] + " " + Cifre.split(" ")[1])
DrugiDomino = str(Cifre.split(" ")[2] + " " + Cifre.split(" ")[3])


ListaPrvogDomina = []
ListadrugogDomina = []


ListaPrvogDomina.append(int(PrviDomino.split(" ")[0]))
ListaPrvogDomina.append(int(PrviDomino.split(" ")[1]))

ListadrugogDomina.append(int(DrugiDomino.split(" ")[0]))
ListadrugogDomina.append(int(DrugiDomino.split(" ")[1]))


Kombinacija = ""

ObeL = ListadrugogDomina + ListaPrvogDomina
NajvecaCifra1 = max(ListaPrvogDomina)
NajmanjaCifra1 = min(ListaPrvogDomina)
NajvecaCifra2 = max(ListadrugogDomina)
NajmanjaCifra2 = min(ListadrugogDomina)
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
        + str(ListaPrvogDomina[0])
        + str(ListaPrvogDomina[1])
        + str(ListadrugogDomina[0])
        + str(ListadrugogDomina[1])
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


NajvecaCifra = max(
    ListaPrvogDomina[0], ListaPrvogDomina[1], ListadrugogDomina[0], ListadrugogDomina[1]
)
# print(NajvecaCifra)
prvaCifra = NajvecaCifra
print(Kombinacija)
