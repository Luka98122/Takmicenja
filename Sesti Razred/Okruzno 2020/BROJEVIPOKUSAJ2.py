from itertools import count

# TEST CASES
# 5 9 11 13 10 12 = 9
# MY TEST CASES
# 1 1 = 1
# 2 1 2 = 2
# 3 10 12 14 = 6
# 5 10 12 14 16 18 = 15


def CounterScore(x):
    rezultat = 0
    for i in range(x + 1):
        rezultat = rezultat + i
    return rezultat


def solve(brojevi):

    neparne = []
    parne = []
    n = len(brojevi)

    for i in range(n):
        if brojevi[i] % 2 == 0:
            parne.append(brojevi[i])
        else:
            neparne.append(brojevi[i])

    counters = []
    counter = 0
    if len(parne) != 0:
        uporodjen1 = parne[0]
        for i in range(len(parne)):

            uporodjen1 = parne[i]

            if i == len(parne) - 1:
                counters.append(counter)
                break

            if uporodjen1 + 2 == parne[i + 1]:
                counter = counter + 1
                if i == 0:
                    counter = counter + 1
            else:
                counters.append(counter)
                counter = 0

    counter = 0
    if len(neparne) != 0:
        uporodjen1 = neparne[0]
        for i in range(len(neparne)):

            uporodjen1 = neparne[i]

            if i == len(neparne) - 1:
                counters.append(counter)
                break

            if uporodjen1 + 2 == neparne[i + 1]:
                counter = counter + 1
                if i == 0:
                    counter = counter + 1
            else:
                counters.append(counter)
                counter = 0

    rezultat = 0
    for i in range(len((counters))):
        rezultat = rezultat + CounterScore(counters[i - 1])
    if len(parne) == 1:
        rezultat = rezultat + 1
    if len(neparne) == 1:
        rezultat = rezultat + 1
    print(rezultat)


TEST_MODE = False
if not TEST_MODE:
    # Read input from stdin
    n = int(input())
    red1 = input().split(" ")
    brojevi = []
    for i in range(n):
        brojevi.append(int(red1[i]))
else:
    # Test case input
    brojevi = [1, 3, 5, 2, 4]

solve(brojevi)
