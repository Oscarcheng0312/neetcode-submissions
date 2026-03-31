class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {} #key is the char and value is the list we wanna return
        for s in strs:
            char_list = sorted(s)
            key = "".join(char_list)

            if key not in freq:
                freq[key] = []

            freq[key].append(s)

        return list(freq.values())


