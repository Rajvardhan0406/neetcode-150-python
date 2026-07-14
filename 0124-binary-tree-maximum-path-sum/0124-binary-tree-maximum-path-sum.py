from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        self.max_sum = float('-inf')
        
        def gain(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            
            through_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, through_path)
            
            return node.val + max(left_gain, right_gain)
        
        gain(root)
        return self.max_sum