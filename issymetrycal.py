# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        a = self.treecheck(root.left)
        b = self.treecheck(self.treeflip(root.right))
        print(a,b, sep="\n")
        return a == b

    def treecheck(self, tree):
        output = []
        if tree is None:
            return output
        else:
            output.append(tree.val)
            output.append(self.treecheck(tree.left))   
            output.append(self.treecheck(tree.right))
            return output
    
    def treeflip(self, tree):
        if tree is None:
            return
        else:
            self.treeflip(tree.left)
            self.treeflip(tree.right)
            tree.left, tree.right = tree.right, tree.left
            return tree

class Solution2(object):
    
    def treeflip(self, tree):
        if tree is None:
            return
        else:
            self.treeflip(tree.left)
            self.treeflip(tree.right)
            tree.left, tree.right = tree.right, tree.left
            return tree
    
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        print(self.treeflip(root.left))
        print(root.right)

        return root.right == self.treeflip(root.left)
    


root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))
#root = TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None)))

s2 = Solution2()
s = Solution()
print(s2.isSymmetric(root)) # Don't use another data structure to work with one you already have...