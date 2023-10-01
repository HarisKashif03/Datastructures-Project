from pathlib import Path
import sys
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.SNode import SNode


class singlyLL:
    def __init__(self, head_node=None):
        if head_node is not None:
            self.head = head_node
            self.tail = head_node
            self.size = 1
            current = head_node
            while current.next:
                current = current.next
            self.tail = current
            self.size += 1
        else:
            self.head = None
            self.tail = None
            self.size = 0

    def InsertHead(self, node):
        if not node:
            return
        
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    
    def InsertTail(self, node):
        if not node:
            return

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1



    def Insert(self, node, position):
        if position < 0:
            raise ValueError("Invalid position")
        elif position == 0:
            node.next = self.head
            self.head = node
            if not self.tail:
                self.tail = node
        else:
            current = self.head
            for i in range(position - 1):
                if not current:
                    raise ValueError("Invalid position")
                current = current.next
            node.next = current.next
            current.next = node
            if not node.next:
                self.tail = node
        self.size += 1


   
    def DeleteHead(self):
        if not self.head:
            return None

        deleted_node = self.head
        self.head = self.head.next
        self.size -= 1

        if not self.head:
            self.tail = None

        deleted_node.next = None
        return deleted_node



    def DeleteTail(self):
        if not self.tail:
            return None
        # if there is only one node in the list
        if self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            self.size = 0
            return temp
        current = self.head
        # find the second-to-last node
        while current.next != self.tail:
            current = current.next
        temp = self.tail
        # remove the last node
        self.tail = current
        self.tail.next = None
        self.size -= 1
        return temp



    def Delete(self, node):
        if not node or not self.head:
            return None
        if self.head == node:
            self.head = node.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return node
        current = self.head
        while current.next and current.next != node:
            current = current.next
        if not current.next:
            return None
        current.next = node.next
        if not current.next:
            self.tail = current
        self.size -= 1
        return node

    

    def Search(self, node, current=None):
        if not current:
            current = self.head
        if not current:
            return None
        if current.data == node.data:
            return current
        return self.Search(node, current.next)



    def isSorted(self):
        if not self.head:
            return True
        current = self.head
        while current.next:
            if current.next.data < current.data:
                return False
            current = current.next
        return True
    

    def SortedInsert(self, node):
        if not node:
            return
        if not node.data:
            return

        if not self.head:
            self.head = node
            self.tail = node
            self.size = 1
        elif not self.isSorted():
            self.Sort()
            self.SortedInsert(node)
        elif node.data <= self.head.data:
            self.InsertHead(node)
        elif node.data >= self.tail.data:
            self.InsertTail(node)
        else:
            current = self.head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
        return None
    

    def Sort(self):
        if not self.head:
            return
        
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        
        nodes.sort(key=lambda node: node.data)
        
        self.head = nodes[0]
        self.tail = nodes[-1]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None



    def Clear(self):
        self.size = 0
        self.head = None
        self.tail = None


    def Print(self):
        if not self.head:
            print("List is empty.")
            return
        print("List length:", self.size)
        if self.isSorted():
                print("Sorted: True")
        else:
            print("Sorted: False")
        current = self.head
        while current:
            print(current.data)
            current = current.next




