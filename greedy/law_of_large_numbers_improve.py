#n,m,k 공백으로 입력받기
n, m, k = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()

largest_value = data[n-1]
second_value = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * largest_value
result += (m-count) * second_value

print(result)
