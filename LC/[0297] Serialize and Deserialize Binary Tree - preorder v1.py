# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    : preorder can uniquely re-construct the binary tree
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        if root is None: return '#'
        return str(root.val)+ ',' + self.serialize(root.left)+ ',' + self.serialize(root.right)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(",")
        N=len(arr)

        def getNum(node):
            if node is None: return 1
            return 1+getNum(node.left)+getNum(node.right)


        def dfs(nodes, curr):
            if nodes[curr] is None: return None

            left = dfs(nodes, curr+1)
            left_sz = getNum(left)
            right = dfs(nodes, curr+left_sz+1)

            nodes[curr].left = left
            nodes[curr].right = right

            return nodes[curr]



        nodes=[]
        for ii in range(N):
            if arr[ii]=='#':
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(arr[ii])))

        return dfs(nodes, 0)









# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
