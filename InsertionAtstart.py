class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def InsertionAtstart(self,newItem):
        NewNode = Node(newItem)  
        NewNode.next =self.head
        self.head=NewNode

linked_list=Linkedlist()
linked_list.head=a=Node("venkat")
a.next=b=Node("sai")
b.next=c=Node("vidya")

linked_list.InsertionAtstart("Madhu")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head=linked_list.head.next