class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        n = len(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for i in nums:
            a[i] += 1
        for num, cnt in a.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, 0 ,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res