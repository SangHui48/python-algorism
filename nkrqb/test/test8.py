# # import queue

# # a = queue.PriorityQueue()
# # a.put(5)
# # a.put(2)
# # a.put(7)
# # a.put(15)
# # a.put(1)

# # while not a.empty():
# #     print(a.get(), end=' ')
# # print()


# a = list(range(10))

# b = []

# while a:
#     b.append(a.pop())
    
# while b:
#     val = b[0]
#     b = b[1:]
#     print(val)

class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next
        
a = Node(1,Node(2,Node(3,Node(4,None))))
b = Node(5,Node(6,Node(7,Node(8,None))))


    

c.next = b

while c:
    print(c.value, end=' ')
    c= c.next


    