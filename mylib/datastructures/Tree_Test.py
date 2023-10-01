from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.TNode import TNode
from mylib.datastructures.Trees.BST import BST
from mylib.datastructures.Trees.AVL import AVL

def main():
    # create a BST using the default constructor
    tree1 = BST()
    print("BST1 root:", tree1.getRoot()) # expected output: None

    # create a BST using the default constructor
    bst_1 = BST()
    print("BST1 root:", bst_1.getRoot()) # expected output: None

    # create a BST using the overload constructor with an integer value
    tree2 = BST(5)
    print("BST2 root:", tree2.getRoot().data) # expected output: 5

    # create a BST using the overload constructor with an integer value
    bst_2 = BST(10)
    print("BST2 root:", bst_2.getRoot().data) # expected output: 10

    # create a TNode with value 3 and use it to create a BST
    node = TNode(3, 0, None, None, None)
    tree3 = BST(node)
    print("BST3 root:", tree3.getRoot().data) # expected output: 3

    # create a TNode with value 7 and use it to create a BST
    node_1 = TNode(7, 0, None, None, None)
    bst_3 = BST(node_1)
    print("BST3 root:", bst_3.getRoot().data) # expected output: 7

    # test the setter and getter for root
    node2 = TNode(7, 0, None, None, None)
    tree1.setRoot(node2)
    print("BST1 root:", tree1.getRoot().data) # expected output: 7

    # test the setter and getter for root
    node_2 = TNode(8, 0, None, None, None)
    bst_1.setRoot(node_2)
    print("BST1 root:", bst_1.getRoot().data) # expected output: 8
    
    print("")
    print("Print BST tree 1 in order:")
    # test the insert() method
    tree2.insert(2)
    tree2.insert(8)
    tree2.insert(4)
    tree2.insert(7)
    tree2.insert(6)
    tree2.insert(1)
    tree2.insert(3)
    tree2.insert(9)
    tree2.printInOrder() # expected output: 1 2 3 4 5 6 7 8 9

    print("")
    print("Print BST tree2 in order:")
    # test the insert() method
    bst_2.insert(2)
    bst_2.insert(15)
    bst_2.insert(5)
    bst_2.insert(12)
    bst_2.insert(9)
    bst_2.insert(1)
    bst_2.insert(4)
    bst_2.insert(17)
    bst_2.printInOrder() # expected output: 1 2 4 5 9 10 12 15 17

    print("")
    print("Print new BST tree 1 in order:")
    # test the insert() method with a TNode argument
    node3 = TNode(10, 0, None, None, None)
    tree2.insert(node3)
    tree2.printInOrder() # expected output: 1 2 3 4 5 6 7 8 9 10

    print("")
    print("Print BST tree 2 in order:")
    # test the insert() method with a TNode argument
    node_3 = TNode(20, 0, None, None, None)
    bst_2.insert(node_3)
    bst_2.printInOrder() # expected output: 1 2 4 5 9 10 12 15 17 20


    print("\n")
    print("Testing search function")

    # test the search() method
    found_node = tree2.search(4)
    print(found_node.data) # expected output: 4
    not_found_node = tree2.search(11)
    print(not_found_node) # expected output: None

    print("")
    print("Testing search function")

    # test the search() method
    found_node = bst_2.search(5)
    print(found_node.data) # expected output: 5
    not_found_node = bst_2.search(25)
    print(not_found_node) # expected output: None

    print("")
    print("Print new BST tree 1 in order:")
    # test the delete() method
    tree2.delete(8)
    tree2.printInOrder() # expected output: 1 2 3 4 5 6 7 9 10-

    print("")
    print("Print new BST tree 2 in order:")
    # test the delete() method
    bst_2.delete(15)
    bst_2.printInOrder() # expected output: 1 2 4 5 9 10 12 17 20

    print("\n")
    print("Deleting values not in the tree:")
    # test the delete() method with a value not in the tree
    tree2.delete(11) # expected output: "Value was not found in the tree."

    # test the delete() method with a value not in the tree
    bst_2.delete(25) # expected output: "Value was not found in the tree."

    print("")
    print("Print new BST tree 1 in printBF:")
    # test the printBF() method
    tree2.printBF() 

    print("")
    print("Print new BST tree 2 in printBF:")
    # test the printBF() method
    bst_2.printBF() 


    # AVL TESTING

    # Create an empty AVL tree
    avl = AVL()

    # Insert some values into the tree
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)

    # Print the tree
    print("\nAVL Tree:\n")
    avl.printInOrder()
    print("")

    # Print the tree
    print("\nAVL Tree: printBF\n")
    avl.printBF()

    # Test the getRoot() method
    print("\nRoot node:\n")
    print(avl.getRoot().data)

    # Test the delete() method
    avl.delete(30)
    avl.delete(50)

    # Print the updated tree
    print("\nUpdated AVL Tree:\n")
    avl.printInOrder()

    # Test inserting a TNode object
    node = TNode(15, 0, None, None, None)
    avl.insert(node)
    print("")

    # Print the updated tree
    print("\nUpdated AVL Tree:\n")
    avl.printInOrder()

    # Test inserting an invalid argument type
    try:
        avl.insert("string")
    except TypeError as e:
        print(e)

    # Test deleting a non-existent value
    result = avl.delete(60)
    if not result:
        print("Value does not exist in the tree.")

    # Print the tree
    print("\nAVL Tree:")
    avl.printInOrder()


    # Create an empty AVL tree
    avl2 = AVL()

    # Insert some values into the tree
    avl2.insert(9)
    avl2.insert(22)
    avl2.insert(51)
    avl2.insert(43)
    avl2.insert(12)

    # Print the tree
    print("\nAVL Tree:\n")
    avl2.printInOrder()
    print("")

    # Print the tree
    print("\nAVL Tree: printBF\n")
    avl2.printBF()

    # Test the getRoot() method
    print("\nRoot node:\n")
    print(avl2.getRoot().data)

    # Test the delete() method
    avl2.delete(22)
    avl2.delete(12)

    # Print the updated tree
    print("\nUpdated AVL Tree:\n")
    avl2.printInOrder()

    # Test inserting a TNode object
    node2 = TNode(15, 0, None, None, None)
    avl2.insert(node2)
    print("")

    # Print the updated tree
    print("\nUpdated AVL Tree:\n")
    avl2.printInOrder()

    # Test inserting an invalid argument type
    try:
        avl2.insert("string")
    except TypeError as e:
        print(e)

    # Test deleting a non-existent value
    result2 = avl2.delete(25)
    if not result2:
        print("Value does not exist")

    # Test deleting a existent value
    avl2.delete(9)

    # Print the tree
    print("\nAVL Tree:")
    avl2.printInOrder()

if __name__ == '__main__':
    main()
