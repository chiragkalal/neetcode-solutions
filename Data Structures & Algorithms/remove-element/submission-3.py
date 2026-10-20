class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[right] == val:
                nums.pop()
                right -= 1
            
            if left < len(nums) and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                nums.pop()
                left += 1
                right -= 1
            else:
                left += 1
        
        return right + 1