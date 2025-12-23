from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: store value with original index
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        
        # Step 2: sort by value
        nums_with_index.sort(key=lambda x: x[0])
        
        # Step 3: two-pointer approach
        i, j = 0, len(nums_with_index) - 1
        while i < j:
            current_sum = nums_with_index[i][0] + nums_with_index[j][0]
            if current_sum == target:
                return [nums_with_index[i][1], nums_with_index[j][1]]  # original indices
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        return []
