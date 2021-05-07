class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)

    # If list is empty
    if l is None:
        return new_node
    
    # insert into head
    if l.value > value:
        new_node.next = l
        return new_node

    # insert into middle
    curr_node = l
    while curr_node is not None:
        if curr_node.next and curr_node.next.value > value:
            # I should insert here!
            new_node.next = curr_node.next
            curr_node.next = new_node
            return l

        curr_node = curr_node.next

    # insert into tail
    curr_node.next = new_node
    return l