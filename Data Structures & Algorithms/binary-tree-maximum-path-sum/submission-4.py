class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(node):
            if node is None:
                return 0

            # 负数贡献会降低路径和，可以不选
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # 在当前节点连接左右两边，更新最终答案
            self.ans = max(
                self.ans,
                left + node.val + right
            )

            # 接到父节点上时，只能选择其中一边
            return node.val + max(left, right)

        dfs(root)
        return self.ans