class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3 2 2 3 2 3] -> val = 3  -> 2 2 2 ...
        non_val_index = 0
        for num in nums:
            if num != val:
                nums[non_val_index] = num
                non_val_index += 1
            else:
                nums[non_val_index] = num
        return non_val_index
        