class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3 2 2 3 2 3] -> val = 3  -> 2 2 2 ...
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                nums.pop()
                right -= 1
            else:
                left += 1
        
        # print(nums)
        return len(nums)

        