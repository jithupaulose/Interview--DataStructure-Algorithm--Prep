Steps:

Or list problem aaanu
namukk first index value
second index = first index value + second index value
third index = first index value + second index value + third index 
so onnn-----

index vech ulla problem aayathu kond range length pidikkam
empty list initialize cheyanam
sum cheynathukond sum um venam

list and sum variable
 loop cheyumbol two steps cheyanam evde
sum il add on cheyanam indexilae values
then append cheyanam value arrayil 

last value return cheyanam.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1 = 0
        value = []
        for i in range(len(nums)):
            sum1 += nums[i]
            value.append(sum1)
        return value
            