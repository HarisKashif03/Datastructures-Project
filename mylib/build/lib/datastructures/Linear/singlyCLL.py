from mylib.datastructures.Linear.singlyLL import singlyLL

class singlyCLL(singlyLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            self.tail.next = head
    
    def InsertHead(self, node):
        super().InsertHead(node)
        self.tail.next = self.head
    
    def InsertTail(self, node):
        super().InsertTail(node)
        self.tail.next = self.head
    
    def Insert(self, node, position):
        if position <= 1:
            self.InsertHead(node)
        elif position > self.size:
            self.InsertTail(node)
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
            self.tail.next = self.head
    
    def DeleteHead(self):
        super().DeleteHead()
        self.tail.next = self.head
    
    def DeleteTail(self):
        if self.head is None:
            return

        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next

        prev.next = self.head
        self.tail = prev
        self.size -= 1

    
    def Delete(self, node):
        current = self.head
        prev = self.tail
        while prev != current:
            if current.data == node.data:
                prev.next = current.next
                self.size -= 1
                if current == self.tail:
                    self.tail = prev
                    prev = current
                return
            current = current.next
        if current.data == node.data:
            prev.next = current.next
            self.size -= 1
            if current == self.tail:
                self.tail = prev


    def Search(self, node, current=None):
            if not current:
                current = self.head
            if not current:
                return None
            if current.data == node.data:
                return current
            if current.next == self.head:
                return None
            return super().Search(node, current.next)

    def SortedInsert(self, node):
            # check if the list is sorted
            if not self.is_sorted():
                # if not sorted, sort the list first
                self.sort()
            # find the proper position to insert the node
            current = self.head
            prev = None
            while current is not None and current.data < node.data:
                prev = current
                current = current.next
            # insert the node at the proper position
            if prev is None:
                self.InsertHead(node)
            else:
                node.next = prev.next
                prev.next = node
                self.size += 1
                if node.next is None:
                    self.tail = node

                    
    def IsSorted(self):
        if self.head is None:
            return True
        current = self.head
        while current.next is not None and current.data <= current.next.data:
            current = current.next
        return current.next is None
       
    def Sort(self):
        if self.head is None or self.head.next is None:
            return  # empty or one node only, already sorted

        last_sorted = self.head  # last node of the sorted sublist
        current = last_sorted.next  # first node of the unsorted sublist

        while current is not self.head:  # traverse the unsorted sublist
            if current.data < last_sorted.data:  # need to insert current node
                # find the correct position to insert current node
                prev = last_sorted
                while prev.next is not current and prev.next.data < current.data:
                    prev = prev.next

                # remove current node from its current position
                last_sorted.next = current.next

                # insert current node at the correct position
                current.next = prev.next
                prev.next = current

                # update last_sorted only if current node was inserted before it
                if prev is last_sorted:
                    last_sorted = current
            else:
                # current node is already in sorted position
                last_sorted = current

            current = last_sorted.next

        self.tail = last_sorted  # update the tail pointer


    def Clear(self):
        super().Clear()  # call the Clear method of the singlyLL class
        self.tail = None  # reset the tail pointer to None


    def Print(self):
            if self.size == 0:
                print("The list is empty.")
                return
            print("List length:", self.size)
            print("Sorted:", "Yes" if self.isSorted() else "No")
            print("List content:", end=" ")
            current = self.head
            for i in range(self.size):
                print(current.data, end=" ")
                current = current.next
            print()


