"""
KEY CONCEPT:
    - Use Element + Linked list data structure for Stack
    - Last in First out
    Activities in Stack:
        + Push. (Insert)
        + Pop. (Remove)
"""
from LinkedList import Element
from LinkedList import LinkedList

class Stack(object):
    def __init__(self, top=None):
        self.stack = LinkedList(head=top)
    
    # Push in stack <=> Insert head in Linked list
    def push(self, newElement):
        if self.stack.head:
            temp = self.stack.head
            self.stack.head = newElement
            self.stack.head.next = temp
        else:
            self.stack.head = newElement

    # Print stack
    def print(self):
        if self.stack.head:
            current = self.stack.head
            print(current.value)
            while current.next:
                print(str(current.value) + "->")
                current = current.next
        else:
            print(self.stack.head)

if __name__ == "__main__":
    top = Element(0)
    element_1 = Element(1)
    stack = Stack(top=top)
    stack.push(element_1)
    stack.print()
            