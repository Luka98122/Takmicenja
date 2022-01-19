stepeni = int(input())
minuti = int(input())
sekundi = int(input())

ukupneSekundi = stepeni * 3600 + minuti * 60 + sekundi
tip = ""
if ukupneSekundi == 90 * 60 * 60:
    tip = "prav"
if ukupneSekundi > 90 * 60 * 60:
    tip = "tup"
if ukupneSekundi < 90 * 60 * 60:
    tip = "ostar"
odgvor = str(ukupneSekundi)
odgvor = odgvor + " " + tip
print(odgvor)
