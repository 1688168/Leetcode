# 20221023
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mxs=float('-inf')
        if root is None: return 0

        def helper(rt):
            nonlocal mxs

            if rt is None: return 0

            left = helper(rt.left)
            right = helper(rt.right)

            curr= max(rt.val+left+right, rt.val+left, rt.val+right, rt.val)
            mxs=max(mxs, curr)

            return rt.val + max(left, right, 0)

        helper(root)
        return mxs


############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mxs=float('-inf')


        def dfs(rt):
            nonlocal mxs
            if rt is None: return 0


            left=max(dfs(rt.left), 0)
            right=max(dfs(rt.right), 0)

            mxs=max(mxs, rt.val+left+right)

            return rt.val + max(left, right)


        dfs(root)

        return mxs