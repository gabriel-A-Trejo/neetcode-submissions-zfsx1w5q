# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, maxValue):
            nonlocal count
            if not root: 
                return None
            
            count += 1 if maxValue <= root.val else 0
            maxValue = max(maxValue, root.val)
            dfs(root.left,  maxValue)
            dfs(root.right, maxValue)
        dfs(root, root.val)
        return count

        