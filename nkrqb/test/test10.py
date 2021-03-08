class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
a = Node(1, Node(2, Node(3, Node(4, None))))
b = Node(5, Node(6, Node(7, Node(8, None))))

# c = Node(a.value, None)
# c.next = Node(b.value, None)
# a = a.next
# b = b.next
# c.next.next = Node(a.value, None)
# c.next.next.next = Node(b.value, None)

# while a.next and b.next:
#     c = Node(a.value, None)
#     c.next = Node(b.value, None)
#     a = a.next
#     b = b.next

c = Node(a.value,None)

# while a.next and b.next:
#     for data in range(3)
#     a = a.next
#     b = b.next
#     data = Node(a.value,Node(b.value,None))
#     c.next.next = data

for i in range(4):
    if a.next == None and b.next == None:
        break
    a = a.next
    b = b.next
    data = Node(a.value, Node(b.value,None))
    
    

while c:
    print(c.value, end=' ')
    c = c.next
    
#1 5 2 6 3 7 4 8 