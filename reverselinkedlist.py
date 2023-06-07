class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def reverse(head):
    prev = None
    current = head

    while current is not None:
        nextNode = current.next
        current.next=prev
        prev = current
        current = nextNode
    return prev
head =a= Node(1)
a.next=b=Node(2)
b.next=c=Node(3)
c.next=d=Node(4)
d.next=e=Node(5)
print("Given linkedlist:")
current=head
while current is not None:
    print(current.item, end=" ")
    current=current.next
head=reverse(head)
print("\n")
print("Reversed linkedlist:")
current=head
while current is not None:
    print(current.item, end=" ")
    current=current.next

