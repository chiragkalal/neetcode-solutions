class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return
            
            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            merge_sort(left)
            merge_sort(right)

            return merge_sorted_arrays(left, right, arr)


        def merge_sorted_arrays(arr_a, arr_b, arr):
            # print("merge_sorted_arrays callend for ", arr_a, arr_b)
            len_a, len_b = len(arr_a), len(arr_b)

            a_index = b_index = arr_index = 0

            while a_index < len_a and b_index < len_b:
                if arr_a[a_index] <= arr_b[b_index]:
                    arr[arr_index] = arr_a[a_index]
                    a_index += 1
                else:
                    arr[arr_index] = arr_b[b_index]
                    b_index += 1
                arr_index += 1
            
            while a_index < len_a:
                arr[arr_index] = arr_a[a_index]
                a_index += 1
                arr_index += 1
            while b_index < len_b:
                arr[arr_index] = arr_b[b_index]
                b_index += 1
                arr_index += 1
        
        merge_sort(nums)
        # print("nums: ", nums)
        return nums


        