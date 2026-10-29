class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3 2 2 3 2 3] -> val = 3  -> 2 2 2 ...
        non_val_index = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[non_val_index] = nums[index]
                non_val_index += 1
            else:
                nums[non_val_index] = nums[index]
        return non_val_index
        