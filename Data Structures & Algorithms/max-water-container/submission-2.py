class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        for i,n1 in enumerate(heights):
            for j in range(i+1,len(heights)):
                area = min(n1,heights[j])*(j-i)
                if area > max_area:
                    max_area = area
        
        return max_area
        
