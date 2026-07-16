class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        ans = []
        start = nums[0]

        for i in range(1, len(nums)):

            # যদি consecutive না হয়
            if nums[i] != nums[i - 1] + 1:

                # Single number
                if start == nums[i - 1]:
                    ans.append(str(start))
                # Range
                else:
                    ans.append(f"{start}->{nums[i - 1]}")

                # নতুন range শুরু
                start = nums[i]

        # শেষ range add করা
        if start == nums[-1]:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{nums[-1]}")

        return ans