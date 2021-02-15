d = [0]*100

def fibo(x):
    if x ==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    # 메모이제이션 기법 적용 = 다이나믹 프로그래밍의 한 기법
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))