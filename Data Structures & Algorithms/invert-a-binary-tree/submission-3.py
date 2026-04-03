# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case 
        # when not root just return None
        if not root: return None

        root.left, root.right = root.right, root.left

        #Flip each side

        #then called the left side
        self.invertTree(root.left)
        self.invertTree(root.right)
        #Then called right side
        return root


        