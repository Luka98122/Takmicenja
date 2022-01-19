prviRed = str(input())
kosta = int(prviRed.split(" ")[0])
placeno = int(prviRed.split(" ")[1])

Kusur = placeno - kosta

if Kusur == 0:
    print(0)
brojPetica = Kusur // 5
brojDvojka = (Kusur % 5) // 2
brojJedinica = (Kusur % 5) % 2

broj = brojPetica + brojDvojka + brojJedinica
print(broj)
