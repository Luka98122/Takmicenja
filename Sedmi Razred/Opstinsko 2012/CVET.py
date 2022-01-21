# TEST CASES
# 5 5 3 9 4 6 = 9
# MY TEST CASES
# 5 1 1 1 1 1 = 5
# 2 4 5 = 3
# 1 100 = 25

import math


papiri = 0
n = int(input())
for i in range(n):
    x = int(input())
    papiri = papiri + math.ceil(x / 4)
print(papiri)
