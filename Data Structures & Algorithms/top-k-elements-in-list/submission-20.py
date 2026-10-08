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
            while buckets[index]:
                if len(freq_elements) == k:
                    return freq_elements
                freq_elements.append(buckets[index].pop())
            if len(freq_elements) == k:
                return freq_elements

        return []   
        