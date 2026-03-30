class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        start, end = 0, 1
        seen = {s[start]: start}
        max_size = 1
        while end < len(s):
            if s[end] in seen:
                if end - start  > max_size:
                    max_size = end - start 
                start = max(seen[s[end]] + 1, start)
            
            seen[s[end]] = end
            end += 1
                
        
        return (end - start ) if (end-start )>max_size else max_size
