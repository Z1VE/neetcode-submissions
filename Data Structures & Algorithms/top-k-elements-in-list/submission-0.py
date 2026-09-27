class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        result = frequency.items()
        return [item[0] for item in sorted(result, key=lambda x: x[1], reverse=True)[:k]]
