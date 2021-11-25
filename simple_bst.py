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
        curr_node = self.root
        if not curr_node: return

        stack = []

        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                print(curr_node.key)
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
