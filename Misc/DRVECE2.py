red1 = input().split(" ")
duzina = int(red1[0])
sirina = int(red1[1])
cestina = int(red1[2])

metoda1 = duzina // cestina * 2 + sirina // cestina * 2
if duzina % 3 == 0 or sirina % 3 == 0:
    metoda1 = metoda1 - 4
print(metoda1)

metoda2 = 