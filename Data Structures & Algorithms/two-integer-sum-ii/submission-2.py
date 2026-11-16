class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 1
        end = len(numbers)

        while start < end:
            cur_sum = numbers[start-1] + numbers[end-1]
            if cur_sum == target:
                return [start, end]
            
            if cur_sum > target:
                end -= 1
            else:
                start += 1
        

        