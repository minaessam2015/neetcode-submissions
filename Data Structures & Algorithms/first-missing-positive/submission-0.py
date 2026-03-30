class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = set()
        for n in nums:
            if n > 0:
                positives.add(n)
        
        if len(positives)==0:
            return 1
        min_num = min(positives)
        max_num = max(positives)
        if min_num > 1:
            return 1

        while min_num <= max_num+1:
            if min_num +1 in positives:
                min_num +=1
            else:
                return min_num+1
        
        return min_num