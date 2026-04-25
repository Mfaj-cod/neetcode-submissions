# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stk = []
        curr = root

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.val)
            curr = curr.right

        return res