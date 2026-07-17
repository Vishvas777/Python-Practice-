class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def second_last(head):
    # List has fewer than 2 nodes
    if head is None or head.next is None:
        return None

    prev = head
    curr = head.next

    while curr.next is not None:
        prev = curr
        curr = curr.next

    return prev.data


# Example
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Second last element:", second_last(head))