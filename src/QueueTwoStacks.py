class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        # lets remove from the out stack, unless its empty
        if len(self.out_stack.items) > 0:
            return self.out_stack.pop()

        # move all items from in_stack to out_stack
        while len(self.in_stack.items) > 0:
            self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()

my_queue = QueueTwoStacks()

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")
my_queue.enqueue("d")

print("The first item added was " + my_queue.dequeue())
print("The second item added was " + my_queue.dequeue())
print("The third item added was " + my_queue.dequeue())
print("The fourth item added was " + my_queue.dequeue())