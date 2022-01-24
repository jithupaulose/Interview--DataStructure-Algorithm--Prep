STEPS:

oru oru basic question aanu
namuk oru list undavvum which is not empty
return aaayi oru copy kuudi kodukanam
1,2,3 - input
1,2,3,1,2,3 - output

just append cheythal mathi or  extend
loop cheykka. append cheykkaa




class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums


#apppend or extend



return nums*2