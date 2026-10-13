class Solution:
    def minWindow(self,s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        ms = defaultdict(int)
        mt = defaultdict(int)
        ansl = -1
        ansr = ns
        if nt > ns:
            return ""

        left = 0
        for i in range(nt):
            mt[t[i]] += 1
        have= 0

        for right in range(ns):
            c = s[right]
            ms[c] += 1
            if c in mt and mt[c] == ms[c]:
                have += 1
            while have == len(mt):
                if left - right > ansl - ansr:
                    ansl ,ansr = left, right
                ms[s[left]] -= 1
                if s[left] in mt and ms[s[left]] < mt[s[left]]:
                    have -= 1
                left += 1
        if ansl == -1:
            return ""
        return s[ansl:ansr+1]            

            

