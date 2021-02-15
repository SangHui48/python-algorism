n = int(input())

array = list(map(int,input().split()))

m = int(input())
find_data = list(map(int,input().split()))

def binary_search(array, target, start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

array.sort()

for data in find_data:
    result = binary_search(array,data,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')