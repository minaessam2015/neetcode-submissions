class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            t = target - numbers[i]
            index = self.binary_search(numbers, t, i+1,len(numbers)-1)
            if index != -1:
                return [i+1,index+1]
        
    
    def binary_search(self,arr, t,s,e)->int:
        if (e-s)<=1:
            if arr[s]==t:
                return s
            if arr[e]==t:
                return e
            return -1

        mid = (s+e)//2
        if arr[mid]==t:
            return mid
        elif arr[mid]>t:
            return self.binary_search(arr,t,s,mid)
        else:
            return self.binary_search(arr, t,mid,e)
        