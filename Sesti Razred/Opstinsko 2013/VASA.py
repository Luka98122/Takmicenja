red1 = input()
cifra1 = int(red1[0])
cifra3 = int(red1[2])
cifra2 = int(red1[1])

pokusaj1 = cifra1 * cifra2 * cifra3
cifre = [cifra1, cifra2, cifra3]
nisuJedinice = []
kolikoJedinica = 0
for i in range(3):
    if cifre[i] == 1:
        kolikoJedinica = kolikoJedinica + 1
    else:
        nisuJedinice.append(cifre[i])
if kolikoJedinica == 1:
    print(1 + nisuJedinice[0] * nisuJedinice[1])
elif kolikoJedinica == 2:
    print(2 * nisuJedinice[1])
if kolikoJedinica == 3:
    print(3)
if kolikoJedinica == 0:
    print(cifra1 * cifra2 * cifra3)
