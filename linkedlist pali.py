class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
def palindrome(head):
    temp= head
    a = []
    palin = True
    while temp != None:
        a.append(temp.item)
        temp = temp.next

    while head != None:
 
        p = a.pop()
        if head.item == p:
            palin = True
        else:
            palin = False
            break

        head = head.next

    return palin

one = Node("a")
one.next=two= Node("c")
two.next=three = Node("d")
three.next=four = Node("d")
four.next=five = Node("c")
five.next=six = Node("a")

result = palindrome(one)
 
print("This is Palindrome:", result)