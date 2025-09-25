# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3,TreeNode(9, None, None),TreeNode(19, TreeNode(22), TreeNode(27)))
    
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if root is None or (root.left is None and root.right is None):
            return True

        # перевірка лівої
        left_ok = True                                
        if root.left is not None:                     
            left_ok = (root.val < root.left.val and self.isBalanced(root.left))

        # перевірка правої
        right_ok = True                           
        if root.right is not None:                  
            right_ok = (root.val < root.right.val and self.isBalanced(root.right))

        return left_ok and right_ok 
    
        
s = Solution()
print(s.isBalanced(root))