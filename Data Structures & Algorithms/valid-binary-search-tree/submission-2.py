# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return (valid(node=node.left, left=left, right=node.val) and
            valid(node=node.right, left=node.val, right=right))
        
        return valid(root, float("-inf"), float("inf"))