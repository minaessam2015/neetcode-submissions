from collections import defaultdict
class Solution:
    def minWindow(self,s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        
        window = defaultdict(int)
        have, need = 0, len(t_count)  # unique chars satisfied
        start = 0
        min_window = float('inf')
        terminals = (-1, -1)
        
        for i, c in enumerate(s):
            window[c] += 1
            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                # record minimum
                if i - start + 1 < min_window:
                    min_window = i - start + 1
                    terminals = (start, i)
                # shrink
                window[s[start]] -= 1
                if s[start] in t_count and window[s[start]] < t_count[s[start]]:
                    have -= 1
                start += 1
        
        return s[terminals[0]:terminals[1]+1] if terminals != (-1,-1) else ""