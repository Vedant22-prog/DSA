from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        result = ""
        
        for ch, freq in count.most_common():
            result += ch * freq
        
        return result