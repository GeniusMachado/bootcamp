from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return print(median(sorted(nums1 + nums2)))
    
Solution().findMedianSortedArrays([1,3,5,7], [2,6,8,11,15,56,1111])  