from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional['TreeNode']) -> str:
        vals = []
        
        def preorder(node: Optional['TreeNode']) -> None:
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(vals)

    def deserialize(self, data: str) -> Optional['TreeNode']:
        vals = iter(data.split(','))
        
        def build() -> Optional['TreeNode']:
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))