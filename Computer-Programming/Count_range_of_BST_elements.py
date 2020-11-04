class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.
                
    def count(self, lo, hi):
        return self.getCount(self.root, lo, hi)

    def getCount(self, ptr, low, high):
        if ptr is None:
            return 0
        elif high >= ptr.item >= low:
            return self.getCount(ptr.left, low, high) + self.getCount(ptr.right, low, high) + 1
        elif ptr.item < low:
            return self.getCount(ptr.right, low, high)
        return self.getCount(ptr.left, low, high)
