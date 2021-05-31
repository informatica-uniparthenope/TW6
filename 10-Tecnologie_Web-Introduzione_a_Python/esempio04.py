# Conditional - Random numbers

import random


x = random.randint(1,100)

print("x:",x)

if x <= 33:
    print("First 3rd")
elif 33 < x <= 66:
    print("Second 3rd")
else:
    print("Third 3rd")
