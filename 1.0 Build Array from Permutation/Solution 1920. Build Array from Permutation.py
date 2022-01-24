Steps:
Idth oru basic question aanu
index vech ulla oru problem
value and and index
evar namukk oru list thannittund

[4,3,2,1] - Input

output il [indexvalue of 4, indexvalue of 3, indexvalue of 2 , indexvalue of 1]

intial aayi oru list undakukaa
index loop cheunadth kond range(len()) vekanam
empty loop il apeend cheykka value ntae index intae value  --- important



class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            final.append(nums[nums[i]])
        return final