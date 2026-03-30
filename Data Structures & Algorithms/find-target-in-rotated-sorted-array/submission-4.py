class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find inflection point
        inflection_point = None
        start, end = 0, len(nums)-1
        
        get_inflection_point = nums[start] > nums[end]
        while get_inflection_point and (start < end):
            mid = start + (end - start)//2
            if nums[mid] < nums[mid-1]:
                inflection_point = mid -1
                break
            if nums[mid] > nums[mid+1]:
                inflection_point = mid 
                break
            if nums[mid] < nums[start]:
                end = mid-1
            else:
                start = mid + 1
            
                


        # find target
        if get_inflection_point:
            if target == nums[inflection_point]:
                return inflection_point
            if target > nums[inflection_point]:
                return -1
            elif target < nums[inflection_point] and target > nums[0]:
                start = 0
                end = inflection_point - 1
            elif target < nums[0]:
                start = inflection_point + 1
                end = len(nums)-1
        else:
            start = 0
            end = len(nums)-1

        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1





