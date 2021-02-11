import random

# 랜덤 리스트 만들기 타입 힌트 추가
array:list = []

for i in range(10):
    num:int = random.randint(1,11)
    array.append(num)

print(array)

#삽입 정렬 시작
for i in range(1,len(array)):
     for j in range(i,0,-1):
         if( array[j] < array[j-1] ):
             array[j],array[j-1] = array[j-1],array[j]
         else:
            break

print(array)