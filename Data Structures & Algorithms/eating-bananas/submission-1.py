class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        l, r = 1, max(piles)
        ans = max(piles)

        while r >= l:
            m = l + ((r - l) // 2)
            temp = 0

            for i in piles:
                temp += (i + m - 1) // m

            if temp > h:
                l = m + 1
            else:
                r = m - 1
                ans = min(ans, m)

        return ans
