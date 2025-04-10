# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        tree1 = self.tree(p)
        tree2 = self.tree(q)
        
        print(tree1, tree2)

        if tree1 == tree2:
            return True
        else:
            return False

    def tree(self, tree):
        
        output = []

        if tree is None:
            return output
        
        if tree.val:
            output.append(tree.val)
        
        if tree.right == 0:
            output.append(0)
        
        if tree.right == None:
            output.append(None)
        
        if tree.right:
            output.extend(self.tree(tree.right))
        
        if tree.left == 0:
            output.append(0)
        
        if tree.left == None:
            output.append(None)
        
        if tree.left:
            output.extend(self.tree(tree.left))
        
        return output

p = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
q = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))

p = TreeNode(1,TreeNode(2,None,None),None)
q = TreeNode(1,None,TreeNode(3,None,None))

p = TreeNode(1,TreeNode(0,None,None),None)
q = TreeNode(1,None,TreeNode(0,None,None))

s = Solution()
print(s.isSameTree(p, q))