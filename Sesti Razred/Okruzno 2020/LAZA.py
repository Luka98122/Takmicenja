# TEST CASES
# 8 7 3 0 1 4 5 6 2 = 3
# MY TEST CASES
# 1 1 = 0
# 5 1 2 3 4 5 = 0
# 3 2 0 1 = 2

n = int(input())
red1 = input().split(" ")
brojevi = []
for i in range(n):
    brojevi.append(int(red1[i]))
# print(sortiraniBrojevi)
kopiLista = brojevi.copy()
sortiranaLista = brojevi.copy()
sortiranaLista.sort()
swaps = 0


for i in range(len(brojevi)):
    if brojevi == sortiranaLista:
        break
    if min(kopiLista) == brojevi[0]:
        del kopiLista[0]
    else:
        a = brojevi.index(min(kopiLista))
        b = i
        brojevi[a], brojevi[b] = brojevi[b], brojevi[a]
        kopiLista[a - swaps], kopiLista[0] = kopiLista[0], kopiLista[a - swaps]
        swaps = swaps + 1
        del kopiLista[0]
print(swaps)
# print(brojevi)
