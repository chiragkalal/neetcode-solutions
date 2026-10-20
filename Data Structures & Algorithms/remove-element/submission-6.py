class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        non_val_index = 0

        for num in nums:
            if num != val:
                nums[non_val_index] = num
                non_val_index += 1
        
        return non_val_index