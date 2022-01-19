red1 = str(input())
duzina = int(red1.split(" ")[0])
sirina = int(red1.split(" ")[1])
Cestina = int(red1.split(" ")[2])
resenje = sirina // Cestina + sirina // Cestina + duzina // Cestina + duzina // Cestina
print(resenje)
