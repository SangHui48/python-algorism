class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
a = Node(1, Node(2, Node(3, Node(4, None))))
b = Node(5, Node(6, Node(7, Node(8, None))))

c = Node(a.value, None)
c.next = Node(b.value, None)
a = a.next
b = b.next
c.next.next = Node(a.value, None)
c.next.next.next = Node(b.value, None)

while a.next and b.next:
    c = Node(a.value, None)
    c.next = Node(b.value, None)
    a = a.next
    b = b.next
    

while c:
    print(c.value, end=' ')
    c = c.next
    
#1 5 2 6 3 7 4 8 