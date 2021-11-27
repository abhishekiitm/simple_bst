class TreeNode():
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self, level=0):
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
            
    def find(self, key):
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