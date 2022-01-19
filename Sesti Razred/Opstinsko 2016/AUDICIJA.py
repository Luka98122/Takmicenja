Vrsta = int(input())
Red1 = str(input())
Glumci = int(Red1.split(" ")[0])
Visoki = int(Red1.split(" ")[1])
Plavooki = int(Red1.split(" ")[2])
Kovrdjavi = int(Red1.split(" ")[3])

if Vrsta == 2:
    rezultat = min(Visoki, Kovrdjavi, Plavooki)
    print(rezultat)
if Vrsta == 1:
    Skup1 = Visoki + Plavooki - Glumci
    skup2 = Skup1 + Kovrdjavi - Glumci
    rezultat = skup2
    print(rezultat)
