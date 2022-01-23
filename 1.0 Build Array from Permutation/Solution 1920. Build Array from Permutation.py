class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            final.append(nums[nums[i]])
        return final