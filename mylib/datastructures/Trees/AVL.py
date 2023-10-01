from pathlib import Path
import sys
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

from mylib.datastructures.nodes.TNode import TNode
from mylib.datastructures.Trees.BST import BST

class AVL(BST):
    def __init__(self, val=None):
        self.root = None
        if val is not None:
            if isinstance(val, int):
                self.root = TNode(val)
            elif isinstance(val, TNode):
                self.root = self.balance(val)

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root
    
    def insert(self, val):
        super().insert(val)
        self.root = self.balance(self.root)

    def delete(self, val):
        super().delete(val)
        self.balance(self.root)
    
    def length(self, node):
        if node is None:
            return -1

        length = 0
        stack = [(node, 1)]

        while stack:
            node, level = stack.pop()

            if node is not None:
                length = max(length, level)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))

        return length - 1

    def balance(self, node):

        if node is None:
            return None
        left_subtree = self.balance(node.left)
        right_subtree = self.balance(node.right)
        balance_factor = self.length(right_subtree) - self.length(left_subtree)
        if balance_factor > 1:
            if self.length(right_subtree.right) < self.length(right_subtree.left):
                right_subtree = self._rotateRight(right_subtree)
            return self._rotateLeft(node)
        elif balance_factor < -1:
            if self.length(left_subtree.left) < self.length(left_subtree.right):
                left_subtree = self._rotateLeft(left_subtree)
            return self._rotateRight(node)
        return node

    def _rotateLeft(self, node):
        roots = node.right
        node.right, roots.left = roots.left, node
        node.balance = self.length(node.right) - self.length(node.left)
        roots.balance = self.length(roots.right) - self.length(roots.left)
        return self._update_parent(node, roots)

    def _rotateRight(self, node):
        roots = node.left
        node.left, roots.right = roots.right, node
        node.balance = self.length(node.right) - self.length(node.left)
        roots.balance = self.length(roots.right) - self.length(roots.left)
        return self._update_parent(node, roots)

    def _update_parent(self, node, roots):
        roots.parent = node.parent
        node.parent = roots
        if roots.left:
            roots.left.parent = node
        if roots.right:
            roots.right.parent = node
        return roots