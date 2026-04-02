class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        for i in range(len(s)):
            if s[i] == "(" or s[i] =="[" or s[i] =="{":
                lst.append(s[i])
            else:
                if len(lst)==0:
                    return False
                if s[i] == ")" and lst[-1]=="(":
                    lst.pop()
                elif s[i] == "]" and lst[-1]=="[":
                    lst.pop()
                elif s[i] == "}" and lst[-1]=="{":
                    lst.pop()
                else:
                    return False
        if len(lst)==0:
            return True
        else:
            return False
                    
        