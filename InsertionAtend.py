class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def InsertionAtend(self,newItem):
        newNode = Node(newItem)
        if self.head == None:
            return newNode
        else:
            lastNode=self.head
            while(lastNode.next):
                lastNode = lastNode.next
            else:
                lastNode.next=newNode

        
linked_list=Linkedlist()
linked_list.head=a=Node("venkat")
a.next=b=Node("sai")
b.next=c=Node("vidya")

linked_list.InsertionAtend("Madhu")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head=linked_list.head.next