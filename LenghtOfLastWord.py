s = "   fly me   to   the moon  "

def lengthOfLastWord(s = str):
    """
    :type s: str
    :rtype: int
    """
    return len(s[::-1].strip().split(" ")[0])

print(lengthOfLastWord(s))