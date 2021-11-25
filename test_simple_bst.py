import unittest
from unittest.case import skip
from simple_bst import BST

class TestSimpleBST(unittest.TestCase):
    def test_insert(self):
        
        key = 1
        
        bst = BST()
        bst.insert(key)
        
        with self.subTest():
            self.assertEqual(bst.root.key, key)

    @unittest.skip("skip this test")
    def test_inorder_walk(self):
        # bst.insert(14)
        # bst.insert(4)
        # bst.insert(7)
        # bst.insert(1)
        # bst.insert(10)
        # bst.insert(6)
        # bst.inorder_walk()
        pass

    def test_find(self):
        bst = BST()
        find_key = 14
        bst.insert(find_key)
        bst.insert(4)
        bst.insert(23)
        with self.subTest("check positive case"):
            self.assertIsNotNone(bst.find(find_key))
        with self.subTest("check negative case"):
            self.assertIsNone(bst.find(10000))