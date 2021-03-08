class Node:
      def __init__(self, value, next):
    self.value = value
    self.next = next

a = Node(1,Node(2,Node(3,Node(4,None))))
b = Node(5,Node(6,Node(7,Node(8,None))))

c = Node(a.value,Node(b.value,None))

for i in range(3):
  node = c
  while node.next:
    node = node.next
  a = a.next
  b = b.next
  c = Node(a.value,Node(b.value,None))
  

while c:
  print(c.value, end=' ')
  c = c.next