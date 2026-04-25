class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        def helper(node):
            if node.left: helper(node.left)
            res.append(node.val)
            if node.right: helper(node.right)
        helper(root)
        
        return res