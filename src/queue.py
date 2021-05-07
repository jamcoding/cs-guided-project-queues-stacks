class LinkedListNode:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = LinkedListNode(value)
        # is the list empty?
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return

    def dequeue(self):
        # is the list empty?
        if self.head is None:
            return
        value = self.head.value
        # remove the node at the head
        self.head = self.head.next
        if self.head is None:
            # no more items
            self.tail = None
        return value

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# print(q.head.value)
# print(q.tail.value)