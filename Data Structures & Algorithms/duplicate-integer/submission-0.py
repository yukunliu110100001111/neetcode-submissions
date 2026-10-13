class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for i in nums:
            if i not in answer:
                answer.add(i)
            else: 
                return True
        return False