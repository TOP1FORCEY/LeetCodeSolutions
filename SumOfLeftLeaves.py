# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total = 0
        
        if not root:
            return 0
        
        if root.left and not root.left.left and not root.left.right:
            total = root.left.val

        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

s = Solution()
print(s.sumOfLeftLeaves(root))