# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
 each parent must be greater than it's left node and less than or equl to the right node 

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, minimum, maximum): 
            
            if not root:
                return True

            if root.val >= maximum:
                return False

            if root.val <= minimum:
                return False 


            left =   dfs(root.left, minimum  , root.val )

            right  =dfs(root.right, root.val, maximum) 
            

            return left and right

        return dfs(root, float("-infinity"), float("infinity") ) 


        