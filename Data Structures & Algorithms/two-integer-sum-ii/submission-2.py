class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s,e = 0, len(numbers)-1
        while s<e:
            total = numbers[s]+numbers[e]
            if total == target:
                return [s+1,e+1]
            elif total > target:
                e -= 1
            else:
                s += 1
