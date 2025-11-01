class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        newC = sorted(c.items(), key=lambda x : -x[1])
        return [i for i, v in newC][:k]