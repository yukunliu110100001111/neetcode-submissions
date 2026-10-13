class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        n = len(nums)
        for i in range(n):
            temp  = target - nums[i]
            if temp in answer:
                return [answer[temp], i]
            else:
                answer[nums[i]] = i 
        return [0,0]