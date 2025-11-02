class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * (N + 1)
        suffix = [1] * (N + 1)
        ans = [0] * N


        for i in range(1, N + 1):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(N - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        prefix = prefix[1:]
        suffix = suffix[:len(suffix)-1]

        for i in range(N):
            if i == 0:
                ans[i] = suffix[1]
            elif i == N - 1:
                ans[i] = prefix[-2]
            else:
                ans[i] = prefix[i - 1] * suffix[i + 1]
        return ans
