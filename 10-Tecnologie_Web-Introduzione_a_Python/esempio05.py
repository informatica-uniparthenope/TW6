# Cycles - While

import random

count =0
x = -1
while x != 50:
    x = random.randint(1, 100)
    count=count+1
    print("count:", count, "x:", x)

print("Done!")