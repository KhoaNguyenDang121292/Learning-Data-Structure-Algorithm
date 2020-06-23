"""
KEY CONCEPT:
    - Use Element + Linked list data structure for Queue
    - First in First out (FIFO)
    Activities in Stack:
        + Enqueue. (Insert to front)
        + Dequeue. (Remove from tail)
        + Front. (Get the front item of Queue)
        + Rear. (Get the last item of Queue)
"""
from LinkedList import LinkedList
from LinkedList import Element

class Queue(object):
    def __init__(self, front=None):
        self.queue = LinkedList(head=front)
    
    def enqueue(self, newElement):
        if self.queue.head:
            current = self.queue.head
            self.queue.head = newElement
            self.queue.head.next = current
        else:
            self.queue.head = newElement

    def dequeue(self):
        if self.queue.head:
            current = self.queue.head
            while current.next:
                current = current.next
            current = None
    
    def print(self):
        if self.queue.head:
            current = self.queue.head
            while current.next:
                print(str(current.value) + "->", end='')
                current = current.next
            if current is not None:
                print(str(current.value))

if __name__ == "__main__":
    front = Element(0)
    queue = Queue(front=front)
    element_1 = Element(1)
    element_2 = Element(2)
    element_3 = Element(3)
    queue.enqueue(element_1)
    queue.enqueue(element_2)
    queue.enqueue(element_3)
    queue.print()
    queue.dequeue()
    queue.print()
