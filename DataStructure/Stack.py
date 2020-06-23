"""
KEY CONCEPT:
    - Use Element + Linked list data structure for Stack
    - Last in First out (LIFO) or First in Last out (FILO)
    Activities in Stack:
        + Push. (Insert)
        + Pop. (Remove)
        + Peek (Get top element of Stack)
        + isEmpty (Check Stack is empty or not)
        + Size (Get size of Stack)
"""
from LinkedList import Element
from LinkedList import LinkedList

class Stack(object):
    def __init__(self, top=None):
        self.top = top
        self.stack = LinkedList(head=top)
    
    # Push in stack <=> Insert head in Linked list
    # Time complexity: O(1)
    def push(self, newElement):
        if self.stack.head:
            temp = self.stack.head
            self.stack.head = newElement
            self.stack.head.next = temp
        else:
            self.stack.head = newElement
    
    # Pop from stack <=> Remove head in Linked list
    # Time complexity: O(1)
    def pop(self):
        if self.stack.head:
            self.stack.head = self.stack.head.next
        else:
            self.stack.head = None

    # Peek get top of Stack
    # Time complexity: O(1)
    def peek(self):
        return self.stack.head

    # Check stack empty
    # Time complexity: O(1)
    def isEmpty(self):
        if self.stack.head:
            return -1
        return 1

    # Get size of Stack
    # Time complexity: O(n)
    def size(self):
        count = 1
        if self.stack.head:
            current = self.stack.head
            while current.next:
                count += 1
                current = current.next
        return count

    # Print stack
    # Time complexity: O(n)
    def print(self):
        if self.stack.head:
            current = self.stack.head
            while current.next:
                print(str(current.value) + "->", end='')
                current = current.next
        else:
            print(self.stack.head)
        print(str(self.top.value), end='')

if __name__ == "__main__":
    top = Element(0)
    element_1 = Element(1)
    element_2 = Element(2)
    stack = Stack(top=top)
    stack.push(element_1)
    stack.push(element_2)
    stack.print()
    print("")
    stack.pop()
    stack.print()
    print("")
    element_3 = Element(3)
    stack.push(element_3)
    stack.print()
    print("")
    element_4 = Element(4)
    stack.push(element_4)
    stack.print()
    print("")
    stack.pop()
    stack.print()
    print("")
    print("Head of Stack: " + str(stack.peek().value))
    isEmpty = "no" if stack.isEmpty() == -1 else "yes"
    print("Stack is empty: " + isEmpty)
    print("Size of Stack: " + str(stack.size()))
