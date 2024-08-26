print("exercise 6")

import random
N = int(input("enter a large number of points: "))
i = 0
count = 0
while count < N:
    x = random.uniform(-1 , 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        i = i + 1
    count = count + 1
pie = 4*i/N
print("the approximate value of pie is", pie)


