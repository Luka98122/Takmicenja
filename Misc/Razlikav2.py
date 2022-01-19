vidjeneCifre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
broj = int(input())
a = int(str(broj)[0])
b = int(str(broj)[1])
c = int(str(broj)[2])
vidjeneCifre[a] = vidjeneCifre[a] + 1
vidjeneCifre[b] = vidjeneCifre[b] + 1
vidjeneCifre[c] = vidjeneCifre[c] + 1

najvecaKomb = ""
najmanjaKomb = ""

for i in range(len(vidjeneCifre)):
    for j in range(vidjeneCifre[9 - i]):
        najvecaKomb = najvecaKomb + str(9 - i)
    for k in range(vidjeneCifre[i]):
        najmanjaKomb = najmanjaKomb + str(i)
print(najvecaKomb)
print(najmanjaKomb)
