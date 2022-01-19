red1 = input().split(" ")
broj1 = int(red1[0])
broj2 = int(red1[1])
broj3 = int(red1[2])
broj4 = int(red1[3])
broj5 = int(red1[4])
broj6 = int(red1[5])


if broj1 == broj2 == broj3 == broj3 == broj5 == broj6:
    print(broj1 * 6)
    exit()


brojevi = [broj1, broj2, broj3, broj4, broj5, broj6]
brojevi.remove(max(brojevi))
brojevi.remove(min(brojevi))
rezultat = 0
for i in range(4):
    rezultat = rezultat + brojevi[i]
print(rezultat)
