class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 4 - k = 2 -> cur_sum - k = diff
        # prev sum dict is used to track continuous sum of index from left to right
        prev_sum = {0: 1}   # for empty sub array for same k element
        cur_sum = 0         # to track current sum
        res_count = 0       # to add counts where we get diff -> cur_sum - k
        
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            # print("Current diff is: ", diff)
            if diff in prev_sum:
                res_count += prev_sum[diff]
            # res_count += prev_sum.get(diff, 0)
            prev_sum[cur_sum] = 1 + prev_sum.get(cur_sum, 0)
            # print("previous sum stored: ", prev_sum)
        
        return res_count



        