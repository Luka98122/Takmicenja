red1 = str(input())
sati = int(red1.split(" ")[0])
minuti = int(red1.split(" ")[1])
sekundi = int(red1.split(" ")[2])

ukupneSekundi = sati * 3600 + minuti * 60 + sekundi
ukupneSekundi = ukupneSekundi - 8 * 3600

ostatakSekundi = ukupneSekundi % 108

if ostatakSekundi < 60:
    print("PROLAZ")
elif ostatakSekundi >= 60 and ostatakSekundi < 64:
    print("CEKAJ")
else:
    print("STANI")
