x = 0
y = 0
red1 = input()
red2 = input()
red3 = input()
p1 = int(red1.split(" ")[0])
p2 = int(red2.split(" ")[0])
p3 = int(red3.split(" ")[0])
r1 = int(red1.split(" ")[1])
r2 = int(red2.split(" ")[1])
r3 = int(red3.split(" ")[1])

ps = [p1, p2, p3]
rs = [r1, r2, r3]

for i in range(3):
    for j in range(4):
        if ps[i] == 1:
            y = y - rs[i]
        if ps[i] == 2:
            x = x + rs[i]
        if ps[i] == 3:
            y = y + rs[i]
        if ps[i] == 4:
            x = x - rs[i]
if x < 0:
    if y < 0:
        print("SZ")
    if y > 0:
        print("JZ")
if x > 0:
    if y < 0:
        print("SI")
    if y > 0:
        print("JI")
if x == 0 or y == 0:
    print("ISTA")
if x == 0 and y == 0:
    print("ISTA")
