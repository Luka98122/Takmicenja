Red1 = str(input())
minuti = int(Red1.split(" ")[0])
sekunde = int(Red1.split(" ")[1])
Mbti = int(Red1.split(" ")[2])
UkupneSekundi = minuti * 60 + sekunde
zauzetiKb = UkupneSekundi * 16
Kilobajti = Mbti * 1024
if Kilobajti >= zauzetiKb:
    print("DA")
else:
    potrebno = zauzetiKb - Kilobajti
    print("NE", potrebno)
