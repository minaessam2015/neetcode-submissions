class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        
        result = []
        for i in range(k):
            max_freq = -1
            max_num = None
            for k,v in d.items():
                if v > max_freq:
                    max_freq = v
                    max_num = k
            result.append(max_num)
            del d[max_num]
        return result

