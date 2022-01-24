STEPS:

Idth oru nalla question aanu
X++ or ++X aaneghil 1  points kittum
--X and X-- aaneghil 1 point pookum
final extra undennanu chodikunadth

if vech cheyyam pattum


Solutions:

First oru variable undakanam with value 0
pine if or vech loop cheyanam add or minus

return the variable


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in operations:
            if (i == "X++") or (i == "++X"):
                ans+=1
            if (i == "X--") or (i == "--X"):
                ans-=1
        return ans
