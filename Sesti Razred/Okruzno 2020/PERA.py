# TEST CASES
# 5 1 2 4 1 5 = 12445
# MY TEST CASES
# 3 3 2 99 = 3 3 99
#
n = int(input())
maks = 0
resenja = []
for i in range(n):
    k = int(input())
    if k > maks:
        maks = k
    resenja.append(maks)
for i in range(n):
    print(resenja[i])
