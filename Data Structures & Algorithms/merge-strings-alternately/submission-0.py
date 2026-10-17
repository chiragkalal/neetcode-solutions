class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        left1, left2 = 0, 0
        len1, len2 = len(word1), len(word2)
        
        while left1 < len1 or left2 < len2:
            if left1 < len1:
                res.append(word1[left1])
                left1 += 1
            if left2 < len2:
                res.append(word2[left2])
                left2 += 1
        
        # print("res: ", res)
        return "".join(res)
        