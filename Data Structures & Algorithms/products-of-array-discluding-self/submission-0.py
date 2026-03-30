class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_pos = set()
        total = 1
        for i,n in enumerate(nums):
            if n ==0:
                zeros_pos.add(i)
                continue
            total*=n
        
        if len(zeros_pos)>1:
            return [0]*len(nums)
        
        total = 1
        for i,n in enumerate(nums):
            if n == 0:
                continue
            total*=n

        if len(zeros_pos)==1:
            result = [0]*len(nums)
            index = zeros_pos.pop()
            result[index] = total
            return result
        
        result = []
        for i,n in enumerate(nums):
            result.append(total//n)
        
        return result
            