Steps
evede questionil two function und . one for self and other the main fucntion. Hintil 2 ennam veman ennu und.
init vech self undakuka. ( question und)
array initalize 0 vekuka
loop for i in range (second funct variable
append cheyka (multiply)
pinnae sum return cheykka

optional array undakenda
sum1 0 aakuka
loop ittu sum1 += cheyukka
return sum1

Method 1:

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        tmp = []
        for i in range(len(self.nums)):
            tmp.append(vec.nums[i]*self.nums[i])
        return sum(tmp)

Method 2: 

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum1 = 0
        for i in range(len(self.nums)):
            sum1 +=(vec.nums[i]*self.nums[i])
        return sum1
        