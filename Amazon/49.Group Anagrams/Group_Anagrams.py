class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        same = collections.defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            same[sorted_word].append(word)
            
        anagrams = sorted(same.values(), key=len, reverse=True)
        return anagrams
            
            
