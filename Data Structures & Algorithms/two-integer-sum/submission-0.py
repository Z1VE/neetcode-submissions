class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, number in enumerate(nums):
            compare = target - number
            if compare in seen:
                return [seen[compare], idx]
            seen[number] = idx