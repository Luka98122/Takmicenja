dan = int(input())
mesec = int(input())
godina = int(input())
prestupna = 0

trazeniDan = dan + 7
trazeniMesec = 1
trazenaGodina = godina

meseciUDanima = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if godina % 4 == 0:
    meseciUDanima[1] = 29
else:
    meseciUDanima[1] = 28
OrdinalDay = trazeniDan
for i in range(mesec - 1):
    OrdinalDay = OrdinalDay + meseciUDanima[i]
print(OrdinalDay)
if OrdinalDay > 365 and godina % 4 != 0:
    OrdinalDay = OrdinalDay - 365
    trazenaGodina = trazenaGodina + 1
elif OrdinalDay > 365:
    OrdinalDay = OrdinalDay - 366
    trazenaGodina = godina + 1
for i in range(mesec):
    if OrdinalDay <= meseciUDanima[i]:
        break

    OrdinalDay = OrdinalDay - meseciUDanima[i]
    trazeniMesec = trazeniMesec + 1

rezultat = str(OrdinalDay) + "." + str(trazeniMesec) + "." + str(trazenaGodina) + "."
print(rezultat)
