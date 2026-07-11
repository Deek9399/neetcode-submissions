class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        if root == None:
            return traversal
        traversal.extend(self.inorderTraversal(root.left))
        traversal.append(root.val)
        traversal.extend(self.inorderTraversal(root.right))
        return traversal