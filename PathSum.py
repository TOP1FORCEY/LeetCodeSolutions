# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, acc):
            
            if not node:
                return False
            
            acc += node.val
            
            if not node.left and not node.right:
                
                return acc == targetSum
            
            return dfs(node.left, acc) or dfs(node.right, acc)
        
        return dfs(root, 0)
        
root = root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
targetSum = 22
        
s = Solution()
print(s.hasPathSum(root, targetSum))

"""
if root == None: 
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right

"""