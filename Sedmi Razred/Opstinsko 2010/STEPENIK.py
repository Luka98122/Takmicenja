# TEST CASES
# 60 25 40 20 30 = 7200
# 1 1 1 1 1 = 4
# 1 1 2 4 5 = 16


duzina = int(input())
sirina1 = int(input())
visina1 = int(input())
sirina2 = int(input())
visina2 = int(input())

gd1 = sirina1 * duzina
gd2 = sirina2 * duzina
sr1a = duzina * visina1
sr2a = sirina1 * visina1
sr1b = duzina * visina2
sr2b = sirina2 * visina2


najboljaMogucnost = (
    duzina * sirina1
    + visina1 * duzina
    + (max(sirina1, visina2) - min(sirina1, visina2)) * duzina
    + visina2 * duzina
    + sirina2 * duzina
)

najboljaMogucnost = najboljaMogucnost
print(najboljaMogucnost)
