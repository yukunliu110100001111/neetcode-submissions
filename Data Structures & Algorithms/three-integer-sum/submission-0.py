class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for left in range(n - 2):
            if nums[left] > 0:
                break

            if left > 0 and nums[left] == nums[left - 1]:
                continue

            pointer = left + 1
            right = n - 1

            while pointer < right:
                total = nums[left] + nums[pointer] + nums[right]

                if total < 0:
                    pointer += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([
                        nums[left],
                        nums[pointer],
                        nums[right]
                    ])

                    pointer += 1
                    right -= 1

                    while pointer < right and nums[pointer] == nums[pointer - 1]:
                        pointer += 1

                    while pointer < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res