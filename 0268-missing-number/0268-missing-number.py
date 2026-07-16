class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        b=len(nums)
        s=(b*(b+1))/2
        return int((s-a))