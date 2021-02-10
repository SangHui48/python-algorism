import random

# 난수 배열 생성
array = []

for i in range(10):
    num = random.randint(1,11)
    array.append(num)

print(array)

# 선택 정렬

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if( array[min_index] > array[j] ):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)