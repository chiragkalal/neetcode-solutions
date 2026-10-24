class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first_candidate = None
        second_candidate = None
        first_count = second_count = 0

        for num in nums:
            if num == first_candidate:
                first_count += 1
            elif num == second_candidate:
                second_count += 1
            elif first_count == 0:
                first_candidate = num
                first_count = 1
            elif second_count == 0:
                second_candidate = num
                second_count = 1
            else:
                first_count -= 1
                second_count -= 1
            
            # print(f"1st cand: {first_candidate} & count: {first_count}")
            # print(f"2nd cand: {second_candidate} & count: {second_count}")
        
        thresold = len(nums) // 3
        # print("thresold: ", thresold)
        result = []

        total_first_count = total_second_count = 0
        for num in nums:
            if num == first_candidate:
                total_first_count += 1
            elif num == second_candidate:
                total_second_count += 1
        
        # print("total first count: ", total_first_count)
        # print("total second count: ", total_second_count)
            
        if total_first_count > thresold:
            result.append(first_candidate)
        if total_second_count > thresold:
            result.append(second_candidate)
        
        return result