class Solution:
    def get_key(self,string):
        d = {ord(c):0 for c in set(string)}
        for c in string:
            d[ord(c)]+=1
        # print(tuple((k,v) for k,v in d.items()))
        total_sum = 0
        # for k,v in d.items():
        #     total_sum*= k+v

        for i,k in enumerate(sorted(d.keys())):
            total_sum+= (i+1)*d[k]*k 
        return total_sum
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            new_set = self.get_key(s)
            # print(s, new_set)

            anagrams[new_set].append(s)
        
        return list(anagrams.values())
        