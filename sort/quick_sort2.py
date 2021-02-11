import random

# 랜덤 리스트 만들기 타입 힌트 추가
array:list = []

for i in range(10):
    num:int = random.randint(1,11)
    array.append(num)

print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))