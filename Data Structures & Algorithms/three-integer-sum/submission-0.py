class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for every pair there will be logn searches
        nums_dict = defaultdict(set)
        for i,n in enumerate(nums):
            nums_dict[n].add(i)
        
        result = set()
        for outer in range(len(nums)):
            for inner in range(outer+1, len(nums)):
                partial = nums[inner] + nums[outer]
                if  -partial in nums_dict:
                    hit1 = 1 if inner in nums_dict[-partial] else 0
                    hit2 = 1 if outer in nums_dict[-partial] else 0
                    if len(nums_dict[-partial]) - (hit1 + hit2) > 0:
                        if hit1:
                            nums_dict[-partial].discard(inner)
                        if hit2:
                            nums_dict[-partial].discard(outer)

                        arr = tuple(sorted(([nums[outer], nums[inner], -partial])))
                        result.add(arr)
                    

                    
        return [list(r) for r in result]



