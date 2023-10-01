from mylib.datastructures.nodes.SNode import SNode
from mylib.datastructures.Linear.singlyLL import singlyLL



class LLStack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
        
    def push(self, data):
        new_node = SNode(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.size -= 1
            return popped_node.data
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
        
    def __len__(self):
        return self.size
