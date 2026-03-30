class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        start,end = 0, len(nums)-1
        pivot = nums[start]
        if nums[start] < nums[end]:
            return pivot
        pivot = None
        while start < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                pivot = nums[mid+1]
                break
            if nums[mid] < nums[mid-1]:
                pivot = nums[mid]
                break
            if nums[mid] > nums[0]:
                # left side
                start = mid + 1
            else:
                end = mid - 1

        return pivot

        