class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -1 0 1 2 -1 -4
        # sort -> -4 -1 -1 0 1 2
            # -> -1 -1 2, -1 0 -1 -> skip second -1 item
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num_i = nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    triplets.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
        
        return triplets


        