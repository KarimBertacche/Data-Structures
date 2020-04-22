import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because it can both insert and remove an element from the queue in 
        # O(1) - constant time complexity
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size <= 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def __len__(self):
        return self.size
