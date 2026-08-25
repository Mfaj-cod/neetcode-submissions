# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        srlz = []
        def dfs(root):
            if not root:
                srlz.append("Null")
                return

            srlz.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(srlz)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(",")
        self.i = 0

        def dfs():
            if tree[self.i] == "Null":
                self.i += 1
                return None

            node = TreeNode(int(tree[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

