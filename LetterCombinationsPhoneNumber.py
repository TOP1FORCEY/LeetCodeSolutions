class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """ 
        numap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        if not digits:
            return []
        
        if len(digits) == 1:
            output = []
            for num in numap[digits]:
                output.append(num)
            return output
            
        else:
            # Start with letters from first digit
            output = numap[digits[0]]
            
            # Loop through remaining digits
            for i in range(1, len(digits)):
                new_output = []
                
                for existing_combination in output:
                    for letter in numap[digits[i]]:
                        new_output.append(existing_combination + letter)
                
                output = new_output
            
            return output
                
        
        
s = "23"
solution = Solution()
print(solution.letterCombinations(s))