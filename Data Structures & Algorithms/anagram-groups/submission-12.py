class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
            a to z -> list -> a at 0 and z at 25 (26)
        """
        group_anagrams = []
        def get_ch_count(string):
            ch_count = [0] * 26
            for ch in st:
                ch_count[ord(ch) - ord("a")] += 1
            return ch_count

        anagrams = {}
        for st in strs:
            st_count = tuple(get_ch_count(st))
            if st_count not in anagrams:
                anagrams[st_count] = [st]
            else:
                anagrams[st_count].append(st)

        return list(anagrams.values())