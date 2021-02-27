# def fun(x, y):
#     # x.append(list(y))
#     x+=list(y)
#     y.append(2)
#     return x

# x = [1,2]
# y = [3, 4]
# z = fun(x, y)
# print(x, y, z)

# a = [1,2,3]
# c = a[:]

# print( a is c, a, c)

# a = int(1)
# b = int(a)
# print( a is b, id(a), id(b))
import copy
a= list[1,2]
b = copy.copy(a)
print(a is b)