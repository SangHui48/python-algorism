n,m = map(int,input().split())

result = 0
while True:
    #n이 k로 나누어 떨어지는 수가 될때까지 빼주기
    target = (n // k ) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
    
    result += 1
    n //= k
    
result += (n - 1)
print(result)
    