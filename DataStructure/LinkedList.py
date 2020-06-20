class Element(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
         
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def add(self, next):
        current = self.head
        if current != None:
            current.next = next
        else:
            current.next = None
    
    def show(self):
        current = self.head
        while current.next:
            print(str(current.value) + "->")
            current = current.next

if __name__ == "__main__":
    head = Element(0, None)
    node_1 = Element(1, None)
    linkedList = LinkedList(head=head)
    linkedList.add(node_1)
    linkedList.show()
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    