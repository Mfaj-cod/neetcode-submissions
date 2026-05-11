class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # dummy node to make edge cases (like head removal) easier
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        # Update tail if the list was empty
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        # Find the node BEFORE the one we want to remove
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        # Remove the node
        node_to_remove = prev.next
        prev.next = node_to_remove.next
        
        # Update tail if we removed the last node
        if node_to_remove == self.tail:
            self.tail = prev
            
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
