# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode] 
        :rtype: int
        """
        if root is None:
            return 0
        else:
            depth1 = self.maxDepth(root.left)
            depth2 = self.maxDepth(root.right)
            return 1 + max(depth1, depth2)



root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))
s = Solution()
print(s.maxDepth(root))