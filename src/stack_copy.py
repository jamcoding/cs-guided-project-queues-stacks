class LinkedListNode:
    def __init__(self, data):
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = LinkedListNode(value)
        # is the list empty?
        if self.head is None:
            self.head = new_node
        else:
            # add to head
            new_node.next = self.head
            self.head = new_node
        return

    def pop(self):
        # is the list empty?
        if self.head is None:
            return
        value = self.head.value
        # remove the node at the head
        self.head = self.head.next
        return value