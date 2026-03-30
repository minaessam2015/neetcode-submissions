class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_in_window = max(nums[:k])
        max_nums = [max_in_window]
        for i in range(k,len(nums)):
            if nums[i] > max_in_window:
                max_in_window = nums[i]
                
            else:
                max_in_window = max(nums[i-k+1:i+1])
            max_nums.append(max_in_window)

        return max_nums
        