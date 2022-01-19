minuti = int(input())
sekunde = int(input())
preostaloMBprePesme = int(input())
ukupnoSekundi = minuti * 60 + sekunde
UkupnoZauzima = ukupnoSekundi * 16
PreostaloUKB = preostaloMBprePesme * 1024 - UkupnoZauzima
ZauzimaMb = PreostaloUKB // 1024
ostatakKb = PreostaloUKB % 1024
print(ZauzimaMb, ostatakKb)

# NE KAZU KAKAV DA BUDE ULAZ FORMATIRAN
# NE VIDI SE ZATO STO JE TEST PRIMER U TABELI
