class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        ans = 0
        res = defaultdict(int)
        for right in range(n):
            if s[right] not in res or res[s[right]] < left:
                res[s[right]] = right
                ans = max(ans, right-left+1)
            else: 
                left = res[s[right]] + 1
                res[s[right]] = right
        return ans

            
