haystack = "ssa2dbutsad"

needle = "sad"

def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
                return -1
        else:
                for i in range(len(haystack)):
                        if i > len(haystack) - len(needle):
                                return -1
                        count = 0
                        for a in range(len(needle)):  
                                if haystack[i + a] == needle[a]:
                                        count += 1
                                        print(haystack[i + a], count) 
                        if count == len(needle):
                                return i


print(strStr(haystack, needle))