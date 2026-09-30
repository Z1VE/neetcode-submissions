class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        current = 1
        nums = sorted(set(nums))
        print(nums)
        if nums == []:
            return 0

        for idx, num in enumerate(nums):
            if idx != len(nums)-1:
                if nums[idx+1] == num + 1:
                    current += 1
                    if current > longest:
                        longest = current
                else:
                    current = 1
        return max(longest,current)