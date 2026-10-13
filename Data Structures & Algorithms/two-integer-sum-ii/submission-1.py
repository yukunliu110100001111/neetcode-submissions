class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            if target - numbers[left] - numbers[right] < 0:
                right -=1
            if target - numbers[left] - numbers[right] == 0:
                return [left+1,right+1]
            if target - numbers[left] - numbers[right] > 0:
                left += 1
        return []