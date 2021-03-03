# import queue

# a = queue.PriorityQueue()
# a.put(5)
# a.put(2)
# a.put(7)
# a.put(15)
# a.put(1)

# while not a.empty():
#     print(a.get(), end=' ')
# print()


a = list(range(10))

b = []

while a:
    b.append(a.pop())
    
while b:
    val = b[0]
    b = b[1:]
    print(val)
    