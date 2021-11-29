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

    def test_inorder_walk(self):
        bst = BST()
        elems = [14, 4, 7, 1, 10, 6]
        for elem in elems:
            bst.insert(elem)
        result = list(bst.inorder_walk())
        self.assertListEqual(result, sorted(elems))

    def test_find(self):
        bst = BST()
        find_key = 14
        bst.insert(find_key)
        bst.insert(4)
        bst.insert(23)
        with self.subTest("check positive case"):
            self.assertIsNotNone(bst.get_node(find_key))
        with self.subTest("check negative case"):
            self.assertIsNone(bst.get_node(10000))

    def test_is_empty(self):
        bst_empty = BST()
        bst_non_empty = BST()
        bst_non_empty.insert(10)
        with self.subTest("check non empty case"):
            self.assertEqual(bst_non_empty.is_empty(), False)
        with self.subTest("check empty case"):
            self.assertEqual(bst_empty.is_empty(), True)

    def test_min_max(self):
        bst = BST()
        elems = [1, 2, 3, 4, 5]
        for elem in elems:
            bst.insert(elem)

        with self.subTest("check maximum"):
            self.assertEqual(bst.max(), max(elems))
        with self.subTest("check minimum"):
            self.assertEqual(bst.min(), min(elems))

    def test__min_max_node(self):
        bst = BST()
        elems = [1, 2, 3, 4, 5]
        for elem in elems:
            bst.insert(elem)

        with self.subTest("check maximum"):
            self.assertEqual(bst._max_node().key, max(elems))
        with self.subTest("check minimum"):
            self.assertEqual(bst._min_node().key, min(elems))

    def test_get_successor_node(self):
        bst = BST()
        elems = [14, 4, 7, 1, 10, 6]
        for elem in elems:
            bst.insert(elem)
        sorted_elems = sorted(elems)
        for idx in range(len(sorted_elems)-1):
            node = bst.get_node(sorted_elems[idx])
            successor_node = bst.get_successor_node(node)
            self.assertEqual(sorted_elems[idx+1], successor_node.key)
        node = bst.get_node(sorted_elems[-1])
        successor_node = bst.get_successor_node(node)
        self.assertIsNone(successor_node)
        
    def test_get_predecessor_node(self):
        bst = BST()
        elems = [14, 4, 7, 1, 10, 6]
        for elem in elems:
            bst.insert(elem)
        sorted_elems = sorted(elems)
        sorted_elems.reverse()
        for idx in range(len(sorted_elems)-1):
            node = bst.get_node(sorted_elems[idx])
            predecessor_node = bst.get_predecessor_node(node)
            self.assertEqual(sorted_elems[idx+1], predecessor_node.key)
        node = bst.get_node(sorted_elems[-1])
        predecessor_node = bst.get_predecessor_node(node)
        self.assertIsNone(predecessor_node)

    def test_delete(self):
        bst = BST()
        elems = [14, 4, 7, 1, 10, 6]
        for elem in elems:
            bst.insert(elem)

        for elem in elems:
            node = bst.get_node(elem)
            bst.delete(node)
            same_node = bst.get_node(elem)
            with self.subTest(elem = elem):
                self.assertIsNotNone(node)
                self.assertIsNone(same_node)