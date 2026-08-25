# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        # returning max path sum without splitting
        def dfs(node):
            if not node:
                return 0
            
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)
            # compute max path sum with split
            res[0] = max(res[0], node.val + leftmax + rightmax)

            return node.val + max(leftmax, rightmax)
        
        dfs(root)
        return res[0]