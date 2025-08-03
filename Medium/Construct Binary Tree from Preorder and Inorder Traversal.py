
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map from value to its index in inorder traversal
        inorder_index_map = {val:ind for ind, val in enumerate(inorder)}
        self.pre_index = 0
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root_val)
            index = inorder_index_map[root_val]
            root.left = helper(in_left, index-1)
            root.right = helper(index+1, in_right)
            return root
        return helper(0, len(inorder)-1)
