class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("#")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split())

        def dfs():
            val = next(values)

            if val == "#":
                return None

            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()