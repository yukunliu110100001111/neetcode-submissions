class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer1 = {}
        answer2 = {}
        for i in s:
            if i in answer1:
                answer1[i] += 1
            else:
                answer1[i] = 1
        for i in t:
            if i in answer2:
                answer2[i] += 1
            else:
                answer2[i] = 1
        return answer1 == answer2
        