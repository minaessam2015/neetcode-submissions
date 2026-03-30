class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        for h in height:
            max_left.append(max(h,max_left[-1]))
        
        max_right = [0]
        for h in height[::-1]:
            max_right = [max(h,max_right[0])] + max_right
        
        total_water = 0
        for i,h in enumerate(height):
            max_left_i = max_left[i]
            max_right_i = max_right[i]
            area = max((min(max_right_i,max_left_i) - h),0)
            total_water+=area
        return total_water


        
        

