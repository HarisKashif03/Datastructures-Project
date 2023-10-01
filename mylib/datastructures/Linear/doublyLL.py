from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.Dnode import DNode

class doublyLL:
    def __init__(self, head=None):
        self.head = None
        self.tail = None
        self.size = 0
        if head:
            self.head = DNode(head)
            self.tail = self.head
            self.size = 1

    def InsertHead(self, node):
        if not node:
            return

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1


    def InsertTail(self, node):
        if not node:
            return

        if not self.tail:
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
        if position == 0:
            self.InsertHead(node)
        elif position == self.size:
            self.InsertTail(node)
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
            if not self.head:
                return None
            deleted_node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1

            deleted_node.next = None
            return deleted_node

    def DeleteTail(self):
        if not self.tail:
            return None
        temp = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
        temp.prev = None
        self.size -= 1
        return temp


    def Delete(self, node):
        if not node or not self.head:
            return None
        
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return node
        
        if self.tail == node:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return node
        
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        self.size -= 1
        return node

    

    def Search(self, node):
        current = self.head
        while current:
            if current == node:
                return current
            current = current.next
        return None
    

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
            current.next.prev = node
            current.next = node
            node.prev = current
            self.size += 1



    def Sort(self):
        if not self.head:
            return

        # Collect all the nodes into a list
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        # Sort the nodes by their data
        nodes.sort(key=lambda node: node.data)

        # Update the links between the nodes
        self.head = nodes[0]
        self.tail = nodes[-1]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]
        nodes[-1].next = None
        nodes[0].prev = None
 


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
            print("List content:")
            current = self.head
            while current:
                print(current.data)
                current = current.next

