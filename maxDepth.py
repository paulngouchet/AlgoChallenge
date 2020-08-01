'''Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
Method - traverse the tree and at each stage increment the depth variable '''

def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return (max(leftDepth, rightDepth) + 1) start at -1 since i will return the depth when i am after the leaf when it null
