class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        unq_nums = {c for c in nums}
        longest = 0
        for n in nums:
            if n-1 not in nums:
                currnet_len = 1
                while n+currnet_len in unq_nums:
                    currnet_len +=1
                if currnet_len > longest:
                    longest = currnet_len
        return longest

        




