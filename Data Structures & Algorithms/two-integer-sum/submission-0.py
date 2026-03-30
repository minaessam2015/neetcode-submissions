class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,n in enumerate(nums):
            if n not in nums_dict:
                nums_dict[n] = []
            nums_dict[n].append(i)
        
        for i,n in enumerate(nums):
            sub = target - n
            if sub in nums_dict:
                for sub_index in nums_dict[sub]:
                    if sub_index == i:
                        continue
                    return [i,sub_index]
        return None