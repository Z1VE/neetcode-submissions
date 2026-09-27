class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodupe = set(nums)
        if len(nodupe) == len(nums):
            return False
        else:
            return True