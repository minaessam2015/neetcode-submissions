class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        s = s.lower()
        while start < end:

            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue 
            
            if s[start] != s[end]:
                return False
            else:
                start +=1
                end -=1
            
        return True