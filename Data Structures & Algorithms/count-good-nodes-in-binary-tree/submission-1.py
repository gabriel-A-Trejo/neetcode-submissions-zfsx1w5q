# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0

            result = 1 if maxValue <= root.val else 0
            maxValue = max(maxValue, root.val)
            result += dfs(root.left, maxValue)
            result += dfs(root.right, maxValue)
            return result
        return dfs(root, root.val)


        