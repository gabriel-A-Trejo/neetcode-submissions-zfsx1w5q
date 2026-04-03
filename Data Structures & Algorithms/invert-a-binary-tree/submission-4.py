# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Edge case if there no root return None
        if not root: return None


        #create a left side and right side and we will flip side then return both side based on it
        #Call funciton to call left or right based on it
        root.left, root.right = root.right, root.left

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root


        