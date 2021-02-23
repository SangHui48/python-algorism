a = ['a', 'b', 'c']
b = {'a', 'c', 'd'}
print(list(set(a).intersection(b)))

while 'b' in list(set(a).difference(b)) :
    print(a)
    a.pop()
    
# while len(a) >= 2 :
#     print(a)
#     a.pop()

# numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# for num in numbers:
#     if num == 4:  # 45
#         print("found : 4!")
#         break
# else:
#     print("Not Found 39...")

# a = (1,2)
# a = a + (1,2)
# print(a)

# a = ['a', 'b', 'c']
# b = {'a', 'c', 'd'}

# print(type(set(a)))