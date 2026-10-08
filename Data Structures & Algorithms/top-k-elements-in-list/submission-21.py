class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for i in range(len(nums)+1)]
        ch_count = {}
        for num in nums:
            ch_count[num] = 1 + ch_count.get(num, 0)
        
        for key, value in ch_count.items():
            buckets[value].append(key)

        freq_elements = []
        for index in range(len(buckets)-1, -1, -1):
            for num in buckets[index]:
                freq_elements.append(num)
                if len(freq_elements) == k:
                    return freq_elements

        return []
        