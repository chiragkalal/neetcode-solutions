class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the last valid elements in both arrays.
        nums1_index = m - 1
        nums2_index = n - 1
        # Last available position in nums1 (including empty slots).
        merge_index = m + n - 1
        # Merge from right to left, placing the larger element first.
        while nums2_index >= 0:

            if (
                nums1_index >= 0
                and nums1[nums1_index] > nums2[nums2_index]
            ):
                nums1[merge_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[merge_index] = nums2[nums2_index]
                nums2_index -= 1

            merge_index -= 1



        