class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if all(x == strs[0] for x in strs):
            return strs[0]

        strs = sorted(strs, key = len, reverse = True)

        first_word = strs.pop(0)
        first_word_len = len(first_word)
        prefix = ""

        for i in range(first_word_len):
            
            count = 0

            for word in strs:
                if i < len(word) and word[i] == first_word[i]:
                    count += 1
                    print(count, word[i])

            if count != len(strs):
                for s in range(i):
                    prefix = prefix + strs[0][s]
                return prefix
            
        return ""