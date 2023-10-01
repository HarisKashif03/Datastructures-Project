from pathlib import Path
import sys
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.TNode import TNode

class BST():
    def __init__(self, val=None, obj=None):
        if obj is not None:
            self.root = obj
        elif val is not None:
            self.root = TNode(val, 0, None, None, None)
        else:
            self.root = None

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def insert(self, val):
        newNode = None
        if isinstance(val, int):
            newNode = TNode(val, 0, None, None, None)
        elif isinstance(val, TNode):
            newNode = val
        else:
            raise TypeError("Invalid argument type. Must be either int or TNode.")
        if self.root is None:
            self.root = newNode
        else:
            self._insert(newNode, self.root)

    def _insert(self, newNode, node):
        if newNode.data < node.data:
            if node.left is None:
                node.left = newNode
                newNode.parent = node
            else:
                self._insert(newNode, node.left)
        elif newNode.data > node.data:
            if node.right is None:
                node.right = newNode
                newNode.parent = node
            else:
                self._insert(newNode, node.right)
        else:
            raise ValueError("Value already exists in the tree.")

    def delete(self, val):
        node = self.root
        parent = None
        while node and node.data != val:
            parent = node
            if val < node.data:
                node = node.left
            else:
                node = node.right
        if not node:
            print("Value was not found in the tree.")
            return
        if not node.left and not node.right:
            if not parent:
                self.root = None
            elif node == parent.left:
                parent.left = None
            else:
                parent.right = None
        elif not node.left:
            child = node.right
            self._replace_node(node, child, parent)
        elif not node.right:
            child = node.left
            self._replace_node(node, child, parent)
        else:
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            self._replace_node(successor, successor.right, parent)

    def _replace_node(self, node, new_node, parent):
        if not parent:
            self.root = new_node
        elif node == parent.left:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node:
            new_node.parent = parent

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, currentNode):
        if currentNode == None:
            return None
        elif val == currentNode.data:
            return currentNode
        elif val < currentNode.data:
            return self._search(val, currentNode.left)
        else:
            return self._search(val, currentNode.right)

    def printInOrder(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            print(node.__str__(), end=" ")
            traverse(node.right)
        traverse(self.root)

    def printBF(self):
        nodes_by_level = []
        current_level = [self.root] if self.root is not None else []
        while current_level:
            nodes_by_level.append(current_level)
            next_level = []
            for node in current_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            current_level = next_level
        for nodes_at_level in nodes_by_level:
            print(*[node.__str__() for node in nodes_at_level], sep=" ")

