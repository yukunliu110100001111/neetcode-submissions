class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0]* n
        post = [0] * n
        res = 0
        for i in range(n - 1 ):
            pre[i+1] = max(pre[i], height[i])
            post[~(i+1)] = max(post[~i], height[~i])
        for i in range(n):
            res += max((min(pre[i],post[i])- height[i]),0)
        return res