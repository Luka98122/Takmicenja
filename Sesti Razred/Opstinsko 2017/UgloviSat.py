sati = int(input())
minuti = int(input())
if sati >= 12:
    sati = sati - 12
MinutStepeni = minuti * 6
SatiStepeni = minuti * 0.5 + sati * 30
rezultat = MinutStepeni - SatiStepeni
if rezultat < 0:
    rezultat = -rezultat
# stepeni = rezultat // 1
minuti = rezultat % 1
minuti = 60 * minuti
praviRezultat = str(int(rezultat)) + ":" + str(int(minuti))
print(praviRezultat)

# TESTED - WORKS
