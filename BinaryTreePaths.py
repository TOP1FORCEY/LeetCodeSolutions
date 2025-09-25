# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return 0
        else:
            depth1 = self.binaryTreePaths(root.left)
            depth2 = self.binaryTreePaths(root.right)
            return 1 + max(depth1, depth2)
        
        
s = Solution()
root = TreeNode(1, TreeNode(3,None, TreeNode(5)), TreeNode(2))
print(s.binaryTreePaths(root))