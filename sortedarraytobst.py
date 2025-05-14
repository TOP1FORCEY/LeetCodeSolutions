class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

arr = [-10,-3,0,5,9]

class Solution(object):
    
    def sortedArrayToBST(self, nums):
        if len(nums) >= 2:
            
            main = nums[len(nums) // 2]
            left = self.sortedArrayToBST(nums[:(len(nums) // 2)])
            right = self.sortedArrayToBST(nums[(len(nums) // 2) + 1:])
            
            node = TreeNode(main, left, right)
            
            return node
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        if not nums:
            return None
        
s = Solution()
print(s.sortedArrayToBST(arr))