# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    output = []
    
    print(root)
    
    if root is None:
        return output

    if root.left:
        output.extend(inorderTraversal(root.left))
    
    output.append(root.val)

    if root.right:
        output.extend(inorderTraversal(root.right))
    
    return output

print(inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))