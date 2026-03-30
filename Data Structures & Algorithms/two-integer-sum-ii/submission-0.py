class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start, end = 0, len(numbers)-1

        while (start < end) and (start >=0) and (end <len(numbers)):
            aggregate = numbers[start]+numbers[end]
            if aggregate == target:
                return [start+1, end+1]
            elif aggregate > target:
                end -= 1
            elif aggregate < target:
                start += 1
        
        