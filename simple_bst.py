from collections import deque

class TreeNode():
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self, level=0):
        # TODO better tree printing
        ret = "\t"*level+repr(self.key)+"\n"
        for child in (self.left, self.right):
            if child is not None:
                ret += child.__repr__(level+1)
        return ret

class BST():
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            return
        
        curr_node = self.root
        prev_node = curr_node.parent
        while curr_node:
            prev_node = curr_node
            if key <= curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if key <= prev_node.key:
            prev_node.left = TreeNode(key, parent=prev_node)
        else:
            prev_node.right = TreeNode(key, parent=prev_node)

    def inorder_walk(self):
        if self.is_empty(): return None
        curr_node = self.root

        stack = []

        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                yield curr_node.key
                curr_node = curr_node.right

    def preorder_walk(self):
        if self.is_empty(): return None
        curr_node = self.root

        stack = []

        while stack or curr_node:
            if curr_node:
                yield curr_node.key
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                curr_node = curr_node.right

    def postorder_walk(self):
        if self.is_empty(): return None
        curr_node = self.root

        stack = []

        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                if not stack or curr_node != stack[-1]:
                    yield curr_node.key
                    curr_node = None
                else:
                    curr_node = curr_node.right

    def levelorder_walk(self):
        if self.is_empty(): return None
        curr_node = self.root

        q = deque()

        while len(q) or curr_node:
            yield curr_node.key
            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)
            curr_node = q.popleft() if len(q) else None

            
    def get_node(self, key):
        curr_node = self.root
        while curr_node:
            if key == curr_node.key :
                return curr_node
            if key <= curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    def is_empty(self):
        return not self.root
    
    def min(self):
        if self.is_empty(): return None
        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node.key

    def max(self):
        if self.is_empty(): return None
        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node.key

    def _min_node(self, curr_node = None):
        """
        returns the minimum node of the subtree rooted at curr_node 
        """
        if self.is_empty(): return None
        if curr_node is None: curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def _max_node(self, curr_node = None):
        """
        returns the minimum node of the subtree rooted at curr_node 
        """
        if self.is_empty(): return None
        if curr_node is None: curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node

    def get_successor_node(self, node):
        """
        returns a node with the smallest key greater than the key of the node
        returns None if node has the largest key in the tree
        """
        if node.right:
            return self._min_node(node.right)
        parent_node = node.parent
        while parent_node and parent_node.right == node:
            node = parent_node
            parent_node = node.parent
        return parent_node

    def get_predecessor_node(self, node):
        """
        returns a node with the greatest key smaller than the key of the node
        returns None if node has the smallest key in the tree
        """
        if node.left:
            return self._max_node(node.left)
        parent_node = node.parent
        while parent_node and parent_node.left == node:
            node = parent_node
            parent_node = node.parent
        return parent_node

    def transplant(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        if new_node:
            new_node.parent = old_node.parent

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor_node = self._min_node(node.right)
            if successor_node.parent != node:
                self.transplant(successor_node, successor_node.right)
                successor_node.right = node.right
                successor_node.right.parent = successor_node
            self.transplant(node, successor_node)
            successor_node.left = node.left
            successor_node.left.parent = successor_node

    def rotate_left(self, node):
        replace_node = node.right
        # swap the appropriate child node
        node.right = replace_node.left
        if node.right: node.right.parent = node

        # link the parents
        replace_node.parent = node.parent
        if node == self.root:
            self.root = replace_node
        elif node.parent.left == node:
            node.parent.left = replace_node
        else:
            node.parent.right = replace_node

        # connect node and replace_node
        replace_node.left = node
        node.parent = replace_node

    def rotate_right(self, node):
        replace_node = node.left
        # swap the appropriate child node
        node.left = replace_node.right
        if node.left: node.left.parent = node

        # link the parents
        replace_node.parent = node.parent
        if node == self.root:
            self.root = replace_node
        elif node.parent.left == node:
            node.parent.left = replace_node
        else:
            node.parent.right = replace_node

        # connect node and replace_node
        replace_node.right = node
        node.parent = replace_node