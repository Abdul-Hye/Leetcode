from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        freq = Counter(nums1)
        ans = []

        for num in nums2:
            if freq.get(num, 0) > 0:
                ans.append(num)
                freq[num] -= 1

        return ans