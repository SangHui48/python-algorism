import random

array = []

for i in range(10):
    num = random.randint(0,10)
    array.append(num)
print(array)

count = [0]*( max(array) + 1 )
print(count)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')