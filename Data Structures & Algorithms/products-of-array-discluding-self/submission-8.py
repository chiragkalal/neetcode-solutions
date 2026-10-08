class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ [1,2,4,6] -> [48,24,12,8]
        step1: Prefix product ->                1  1  2 8
        step2: Postfix product -> 1 6 24 48 ->  48 24 6 1
               final ans -> 
        """

        prefix, postfix = 1, 1
        res_list = [1]

        for pre_index in range(len(nums)-1):
            prefix *= nums[pre_index]
            res_list.append(prefix)
        
        for post_index in range(len(nums)-1, -1, -1):
            res_list[post_index] *= postfix
            postfix *= nums[post_index]
        
        return res_list
