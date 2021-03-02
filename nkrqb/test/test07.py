# a = ['a', 'b', 'c', 'd', 'e', 'f']
# b = [1, 2, 3, 4, 5, 6]

# for i in range(5):
#     a[i:], b[i:] = b[i:], a[i:]
#     print(a + b)

import array

init = [1,2,3,4,5]
a = array.array('i', init)
b = array.array('i', [0]*len(a)*2)

b[:len(a)] = a
b[len(a):] = array.array('i',[6,7,8,9,10])

print(b)
print(a)