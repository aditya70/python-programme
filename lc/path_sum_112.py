# Definition for a binary tree node.
from operator import truediv


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        __init__
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
       return self.pathSum(root, 0, targetSum)

    def pathSum(self, root, curr, target) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and curr+root.val==target:
            return True
        return self.pathSum(root.left, curr+root.val, target) or self.pathSum(root.right, curr+root.val, target)  
