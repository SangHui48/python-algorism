import random

# 랜덤 리스트 만들기 타입 힌트 추가
array:list = []

for i in range(10):
    num:int = random.randint(1,11)
    array.append(num)

print(array)

def quick_sort(array, start, end):
    if(start >= end):
        return
    pivot = start
    left = start + 1
    right = end
    
    while(left <= right):
        while(left <= end and array[left] <= array[pivot])
    