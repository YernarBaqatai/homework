class Solution:
    def numIdenticalPairs(self, nums: List[int])-> int:
        count = 0
        N = len(nums)

        for index in range(N):
            for index2 in range(index + 1, N):
                if nums[index] == nums[index2]:
                    count += 1
        return count