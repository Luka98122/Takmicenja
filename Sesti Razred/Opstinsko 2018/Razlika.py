broj = int(input())
a = int(str(broj)[0])
b = int(str(broj)[1])
c = int(str(broj)[2])
cifre = []
cifre.append(a)
cifre.append(b)
cifre.append(c)

nule = 0
for i in range(3):
    if cifre[i] == 0:
        nule = nule + 1

rezultat = 0
najvecaCifra = max(a, b, c)
najmanjaCifra = min(a, b, c)
srednjaCifra = a + b + c - (najvecaCifra + najmanjaCifra)

najvecaKomb = str(najvecaCifra) + str(srednjaCifra) + str(najmanjaCifra)

najmanjaKomb = str(najmanjaCifra) + str(srednjaCifra) + str(najvecaCifra)

if nule == 2:
    rezultat = 0
    print(rezultat)
    exit()
if nule == 1:
    najmanjaKomb = str(srednjaCifra) + str(najmanjaCifra) + str(najvecaCifra)
rezultat = int(najvecaKomb) - int(najmanjaKomb)
print(rezultat)
