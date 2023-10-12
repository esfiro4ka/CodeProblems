from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#1
        result = []
        min_len = min(len(nums1), len(nums2))
        if min_len == len(nums1):
            for i in range(min_len):
                if nums1[i] in nums2:
                    result.append(nums1[i])
                    nums2.remove(nums1[i])
        else:
            for i in range(0, min_len):
                if nums2[i] in nums1:
                    result.append(nums2[i])
                    nums1.remove(nums2[i])
        return result
#2    
        # counter1 = Counter(nums1)
        # counter2 = Counter(nums2)
        # return list((counter1 & counter2).elements())
                    