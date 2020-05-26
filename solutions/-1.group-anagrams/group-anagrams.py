class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_dict = dict()
        for item in strs:
            item_hash = 1
            for char in item:
                item_hash *= (ord(char) + 10000)
            hash_dict[item_hash] = hash_dict.get(item_hash, []) + [item]
        res = [value for value in hash_dict.values()]
        return res