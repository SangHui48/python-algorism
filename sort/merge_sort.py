import random

array = []

for i in range(10):
    num = random.randint(0, 10)
    array.append(num)

print(array)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_arr = merge_sort(array[:mid])
    right_arr = merge_sort(array[mid:])

    merge_arr = []

    l = r = 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merge_arr.append(left_arr[l])
            l += 1
        else:
            merge_arr.append(right_arr[r])
            r += 1

    merge_arr += left_arr[l:]
    merge_arr += right_arr[r:]

    return merge_arr


print(merge_sort(array))
