from pathlib import Path
import sys
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

from mylib.datastructures.Linear.doublyLL import doublyLL
from mylib.datastructures.nodes.Dnode import DNode


class doublyCLL(doublyLL):
    def __init__(self):
        super().__init__()
        self.head = DNode(None)
        self.tail = DNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head

    
    def InsertHead(self, node):
        super().InsertHead(node)
        self.head.next.prev = self.tail
        self.tail.next = self.head.next
    
    def InsertTail(self, node):
        super().InsertTail(node)
        self.tail.next = self.head.next
        self.head.next.prev = self.tail
    
    def Insert(self, node, position):
        if position <= 1:
            self.InsertHead(node)
        elif position > self.size:
            self.InsertTail(node)
        else:
            current = self.head
            for i in range(position):
                current = current.next
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            self.size += 1


    def DeleteHead(self):
        if self.size > 0:
            super().DeleteHead()
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
    
    def DeleteTail(self):
        if self.size > 0:
            super().DeleteTail()
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
    
    def Delete(self, node):
        if node == self.head or node == self.tail:
            return
        else:
            super().Delete(node)


    def Search(self, node):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == node.data:
                return current
            if current == self.tail:
                return None
            current = current.next

    
    def IsSorted(self):
        if self.head is None:
            return True
        current = self.head
        while current.next is not None and current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    
    
    def SortedInsert(self, node):
            if self.head == None:
                self.InsertHead(node)
                return
            else:
                if self.isSorted == False:
                    self.Sort()
                current = self.head.next
                while current != self.head and current.data != None and node.data > current.data:
                    current = current.next
                node.next = current
                node.prev = current.prev
                current.prev.next = node
                current.prev = node
                self.size += 1


    def Sort(self):
        if self.isSorted:
            return
        else:
            for i in range(2, self.size+1):
                node = self.head.next
                for j in range(1, i):
                    if node.next.data < node.data:
                        temp = node.data
                        node.data = node.next.data
                        node.next.data = temp
                    node = node.next
            self.isSorted = True
    
    def Clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size = 0
        self.isSorted = False
    
    def Print(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            print("List length:", self.size)
            if self.isSorted:
                print("List is sorted")
            else:
                print("List is not sorted")
            current = self.head.next
            while current != self.tail:
                print(current.data)
                current = current.next
