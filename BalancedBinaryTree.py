# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root1 = TreeNode(3,TreeNode(9, None, None),TreeNode(19, TreeNode(22), TreeNode(27)))

root2 = TreeNode(1, TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))

class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        
        
    
    
    
    
s = Solution()
print(s.isBalanced(root1))