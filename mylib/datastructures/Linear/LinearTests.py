from pathlib import Path
import sys
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.SNode import SNode
from mylib.datastructures.nodes.Dnode import DNode
from mylib.datastructures.Linear.singlyLL import singlyLL
from mylib.datastructures.Linear.doublyLL import doublyLL
from mylib.datastructures.Linear.singlyCLL import singlyCLL
from mylib.datastructures.Linear.doublyCLL import doublyCLL
from mylib.datastructures.Linear.LLQueue import LLQueue
from mylib.datastructures.Linear.LLStack import LLStack


def main():
    # Test singly linked list
    # create a new singly linked list
    sLL = singlyLL()

    # insert some nodes
    sLL.InsertHead(SNode(1))
    sLL.InsertHead(SNode(2))
    sLL.InsertHead(SNode(3))
    sLL.InsertHead(SNode(4))
    sLL.InsertTail(SNode(5))
    sLL.InsertTail(SNode(6))

    # print the list
    sLL.Print()  # expect: 4 3 2 1 5 6

    # test search functionality
    node = sLL.Search(SNode(3))
    print(node.data)  # expect: 3

    # test deletion functionality
    sLL.Delete(SNode(3))
    sLL.DeleteHead()
    sLL.DeleteTail()
    sLL.Print()  # expect: 2 1 5

    # test sorted insert functionality
    sLL.SortedInsert(SNode(3))
    sLL.SortedInsert(SNode(4))
    sLL.Print()  # expect: 2 1 3 4 5

    # test sorting functionality
    sLL.InsertHead(SNode(8))
    sLL.InsertHead(SNode(6))
    sLL.InsertHead(SNode(7))
    sLL.InsertHead(SNode(9))
    sLL.InsertHead(SNode(10))
    sLL.Print()  # expect: 10 9 7 6 8 2 1 3 4 5
    sLL.Sort()
    sLL.Print()  # expect: 1 2 3 4 5 6 7 8 9 10

    # test clear functionality
    sLL.Clear()
    sLL.Print()  # expect: List is empty





    print("fthhrhtyhfesf")









    #Test doubly linked list
    # Create doubly linked list
    dll = doublyLL()

    # Test InsertHead and InsertTail
    dll.InsertHead(DNode(1))
    dll.InsertTail(DNode(3))
    dll.InsertHead(DNode(2))
    dll.Print()  # List length: 3, List is not sorted, 2 1 3

    # Test Insert
    dll.Insert(DNode(4), 4)
    dll.Insert(DNode(0), 1)
    dll.Print()  # List length: 5, List is not sorted, 0 2 1 3 4

    # Test SortedInsert
    dll.SortedInsert(DNode(5))
    dll.SortedInsert(DNode(-1))
    dll.Print()  # List length: 7, List is sorted, -1 0 1 2 3 4 5

    # Test DeleteHead, DeleteTail, and Delete
    dll.DeleteHead()
    dll.DeleteTail()
    dll.Delete(DNode(2))
    dll.Print()  # List length: 4, List is sorted, 0 1 3 4

    # Test size method
    print("Size:", dll.size)  # Size: 4










    #Test singly circular linked list
    # Create a new singlyCLL object
    scll = singlyCLL()

    # Test InsertHead
    scll.InsertHead(SNode(1))
    scll.InsertHead(SNode(2))
    scll.InsertHead(SNode(3))

    # Test InsertTail
    scll.InsertTail(SNode(4))
    scll.InsertTail(SNode(5))
    scll.InsertTail(SNode(6))

    # Test Insert
    scll.Insert(SNode(7), 4)
    scll.Insert(SNode(8), 1)
    scll.Insert(SNode(9), 9)

    # Test DeleteHead
    scll.DeleteHead()

    # Test DeleteTail
    scll.DeleteTail()

    # Test Delete
    scll.Delete(SNode(5))
    scll.Delete(SNode(10))

    # Test Print
    scll.Print()












    # create a new doublyCLL object
    dcll = doublyCLL()

    # test InsertHead(node) and InsertTail(node)
    dcll.InsertHead(DNode(1))
    dcll.InsertTail(DNode(2))
    dcll.InsertHead(DNode(0))
    dcll.Print()  # expected output: List length: 3 \n List is not sorted \n 0 \n 1 \n 2

    # test Insert(node, position)
    dcll.Insert(DNode(5), 2)
    dcll.Insert(DNode(3), 1)
    dcll.Print()  # expected output: List length: 5 \n List is not sorted \n 0 \n 3 \n 1 \n 5 \n 2

    # test SortedInsert(node)
    dcll.SortedInsert(DNode(4))
    dcll.SortedInsert(DNode(-1))
    dcll.Print()  # expected output: List length: 7 \n List is sorted \n -1 \n 0 \n 1 \n 2 \n 3 \n 4 \n 5

    # test Search(node)
    node = dcll.Search(DNode(2))
    print(node.data)  # expected output: 2
    node = dcll.Search(DNode(6))
    print(node)  # expected output: None

    # test DeleteHead()
    dcll.DeleteHead()
    dcll.Print()  # expected output: List length: 6 \n List is sorted \n 0 \n 1 \n 2 \n 3 \n 4 \n 5

    # test DeleteTail()
    dcll.DeleteTail()
    dcll.Print()  # expected output: List length: 5 \n List is sorted \n 0 \n 1 \n 2 \n 3 \n 4

    # test Delete(node)
    dcll.Delete(dll.head.next)
    dcll.Delete(dll.tail.prev)
    dcll.Print()  # expected output: List length: 3 \n List is sorted \n 1 \n 2 \n 3

    # test Sort()
    dcll.Sort()
    dcll.Print()  # expected output: List length: 3 \n List is sorted \n 1 \n 2 \n 3

    # test Clear()
    dcll.Clear()
    dcll.Print()  # expected output: List is empty






# create an empty queue
    q = LLQueue()

    # test is_empty method on an empty queue
    assert q.is_empty() == True

    # enqueue some elements
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # test is_empty method on a non-empty queue
    assert q.is_empty() == False

    # test peek method
    assert q.peek() == 1

    # test dequeue method
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    # test len method
    assert len(q) == 1

    # enqueue some more elements
    q.enqueue(4)
    q.enqueue(5)

    # test dequeue method
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5

    # test is_empty method on an empty queue
    assert q.is_empty() == True

    # test exception on empty dequeue
    try:
        q.dequeue()
        assert False, "Expected an exception"
    except:
        pass







    # Create a new empty stack
    stack = LLStack()

    # Test is_empty() method
    assert stack.is_empty() == True

    # Test push() method
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert len(stack) == 3

    # Test pop() method
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert len(stack) == 2

    # Test popping all elements until stack is empty
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == None
    assert stack.peek() == None
    assert len(stack) == 0
    assert stack.is_empty() == True

    # Test pushing and popping with empty stack
    assert stack.pop() == None
    stack.push(4)
    assert stack.pop() == 4
    assert stack.is_empty() == True


if __name__ == '__main__':
    main()