class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twen=0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            elif bills[i]==20:
                if ten>=1 and five>=1:
                    twen+=1
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                    twen+=1
                else:
                    return False
        if five>=0 and ten>=0:
            return True
        else:
            return False
        