class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if (num - 1) not in nums_set:
                cur_len = 1
                # print(f"cur num: {num} with its cur len: {cur_len}")
                while num + cur_len in nums_set:
                    cur_len += 1
                    # print(f"{num-1} is present so increase cur len: {cur_len}")
            
                max_len = max(cur_len, max_len)
            # print(f"Updating max value to {max_len}")
        
        return max_len
            
        