# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        def dfs(node: TreeNode) -> int:
            if node is None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest, left + right + 2)
            
            return 1 + max(left, right)
        print(dfs(root))
        return self.longest