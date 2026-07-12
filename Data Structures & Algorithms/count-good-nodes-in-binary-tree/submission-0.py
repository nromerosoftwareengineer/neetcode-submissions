# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        goodNodes = [0]

        def dfs(root, rootval, goodNodes):
                if not root:
                    return 

                if root.val >= rootval:
                    goodNodes[0] +=1

                rootval = max(rootval, root.val)
                dfs(root.left, rootval, goodNodes)

                dfs( root.right, rootval, goodNodes) 

        dfs(root, float("-infinity"), goodNodes)


        return goodNodes[0]