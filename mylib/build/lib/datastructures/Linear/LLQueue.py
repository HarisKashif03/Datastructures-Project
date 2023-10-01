from mylib.datastructures.nodes.SNode import SNode
from mylib.datastructures.Linear.singlyLL import singlyLL



class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = SNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data

    def __len__(self):
        return self.size
