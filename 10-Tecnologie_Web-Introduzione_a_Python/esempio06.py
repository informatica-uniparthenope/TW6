# Cycles - For

import random

n = 10000
m = 0
l = 1000
for i in range(n):

    count = 0
    x = -1
    while x != l:
        x = random.randint(1, l)
        count=count+1
    m=m+count

print("Done! average:", m/n)