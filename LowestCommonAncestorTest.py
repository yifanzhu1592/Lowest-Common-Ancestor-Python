import unittest

import LowestCommonAncestor as lca

class LowestCommonAncestorTest(unittest.TestCase):
    # tree functions
    #      0
    #    /   \
    #   1     2
    #  / \   / \
    # 3   4 5   6
    def testTree(self):
        tree = lca.LowestCommonAncestor.binaryTree()

        # empty tree
        assert tree.getKey(tree.head) == -1

        # head
        tree.add(0, None, True)
        assert tree.getKey(tree.head) == 0

        # children of the head
        tree.add(1, tree.head, True)
        tree.add(2, tree.head, False)
        assert tree.getKey(tree.head.lChild) == 1
        assert tree.getKey(tree.head.rChild) == 2

        # children of the children of the head
        tree.add(3, tree.head.lChild, True)
        tree.add(4, tree.head.lChild, False)
        tree.add(5, tree.head.rChild, True)
        tree.add(6, tree.head.rChild, False)
        assert tree.getKey(tree.head.lChild.lChild) == 3
        assert tree.getKey(tree.head.lChild.rChild) == 4
        assert tree.getKey(tree.head.rChild.lChild) == 5
        assert tree.getKey(tree.head.rChild.rChild) == 6

    # valid LCA
    #      0
    #    /   \
    #   1     2
    #  / \   / \
    # 3   4 5   6
    def testLCA(self):
        tree = lca.LowestCommonAncestor.binaryTree()

        tree.add(0, None, True)
        tree.add(1, tree.head, True)
        tree.add(2, tree.head, False)
        tree.add(3, tree.head.lChild, True)
        tree.add(4, tree.head.lChild, False)
        tree.add(5, tree.head.rChild, True)
        tree.add(6, tree.head.rChild, False)

        # LCA of 0 and 0
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head, tree.head) == 0

        # LCA of 1 and 2
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head.lChild, tree.head.rChild) == 0

        # LCA of 1 and 6
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head.lChild, tree.head.rChild.rChild) == 0

        # LCA of 3 and 6
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head.lChild.lChild, tree.head.rChild.rChild) == 0

        # LCA of 1 and 4
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head.lChild, tree.head.lChild.rChild) == 1

        # LCA of 3 and 4
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head.lChild.lChild, tree.head.lChild.rChild) == 1

    # invalid LCA
    #      0
    #    /   \
    #   1     2
    #  / \   / \
    # 3   4 5   6
    def testInvalid(self):
        tree = lca.LowestCommonAncestor.binaryTree()

        tree.add(0, None, True)
        tree.add(1, tree.head, True)
        tree.add(2, tree.head, False)
        tree.add(3, tree.head.lChild, True)
        tree.add(4, tree.head.lChild, False)
        tree.add(5, tree.head.rChild, True)
        tree.add(6, tree.head.rChild, False)

        # LCA of 0 and an empty node
        assert lca.LowestCommonAncestor.getLCA(tree, tree.head, None) == -1

        # LCA of two empty nodes
        assert lca.LowestCommonAncestor.getLCA(tree, None, None) == -1


if __name__ == '__main__':
    unittest.main()