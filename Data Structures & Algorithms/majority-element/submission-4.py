class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = {}
        majority_cond = len(nums) / 2

        for num in nums:
            if num in nums_count:
                nums_count[num] = 1 + nums_count.get(num)    
            else:
                nums_count[num] = 1
            
            if nums_count[num] >= majority_cond:
                return num