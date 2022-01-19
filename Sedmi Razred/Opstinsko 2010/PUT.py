sirina = int(input())
duzina = int(input())

s1 = int(input())
s2 = int(input())

moguce = []
if duzina % s1 == 0 and sirina % s1 == 0:
    moguce.append(s1)
if duzina % s2 == 0 and sirina % s2 == 0:
    moguce.append(s2)
if moguce == []:
    print("NE MOZE")
    exit()
najveca = max(moguce)
print(int(sirina / najveca * duzina / najveca))
