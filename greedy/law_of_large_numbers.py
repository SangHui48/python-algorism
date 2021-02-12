#n,m,k 공백으로 입력받기
n, m, k = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()

largest_value = data[n-1]
second_value = data[n-2]
sum = 0
count = 1

for i in range(m):
    if count <= k:
        sum += largest_value
        count += 1
    else:
        sum += second_value
        count = 1

print(sum)
