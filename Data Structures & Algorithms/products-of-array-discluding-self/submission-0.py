class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]* n
        post = [1] * n
        result = [1] * n
        for i in range(n-1):
            pre[i+1] = pre[i]* nums[i]
            post[~(i+1)] = post[~i]* nums[~i]
        for i in range(n):
            result[i] = pre[i] * post[i]
        return result