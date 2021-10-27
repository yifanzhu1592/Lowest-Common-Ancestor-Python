class LowestCommonAncestor(object):

    # return the key of the LCA of the two nodes
    @staticmethod
    def getLCA(theTree, val1, val2):
        if val1 is None or val2 is None:
            return -1

        route1 = []
        route2 = []
        node1 = val1
        node2 = val2

        condition = True
        while condition:
            route1.append(node1.key)
            node1 = node1.parent
            condition = node1 is not None

        condition = True
        while condition:
            route2.append(node2.key)
            node2 = node2.parent
            condition = node2 is not None

        for theNode in route1:
            for searchNode in route2:
                if theNode is searchNode:
                    return int(theNode)

        return -1

    # the binary tree that we will be traversing
    class binaryTree(object):

        def __init__(self):
            self.head = None

        def getKey(self, theNode):
            if theNode is not None:
                return theNode.key
            return -1

        def add(self, key, parent, isLeft):
            newNode = self.treeNode(key, parent, None, None)
            if self.head is None:
                self.head = newNode
                return
            if isLeft:
                parent.lChild = newNode
            else:
                parent.rChild = newNode

        class treeNode(object):

            def __init__(self, key, parent, lChild, rChild):
                self.key = key
                self.parent = parent
                self.lChild = lChild
                self.rChild = rChild
