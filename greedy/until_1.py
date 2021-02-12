n,m = map(int,input().split())

count = 0
while True:
    if n % m != 0:
        n -= 1
        count += 1
    else:
        n = n // m
        count += 1
    if n == 1:
        print(count)
        break