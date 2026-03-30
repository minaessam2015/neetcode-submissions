import string
class Solution:
    def isAnagram_old(self, s: str, t: str) -> bool:
        s_dict = {c:0 for c in string.ascii_lowercase}
        t_dict = {c:0 for c in string.ascii_lowercase}
        for c in s:
            s_dict[c]+=1
        for c in t:
            t_dict[c]+=1
        for c in s_dict:
            if t_dict[c] != s_dict[c]:
                return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {c:0 for c in string.ascii_lowercase}
        for c in s:
            s_dict[c]+=1
        for c in t:
            s_dict[c]-=1
            # if s_dict[c]<0:
            #     return False
        for c in s_dict:
            if  s_dict[c] !=0:
                return False
        return True


            
        