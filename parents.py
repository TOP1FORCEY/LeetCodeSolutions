s = "()[]}"

def function(s):

    if s.count("(") - s.count(")") == 0 and s.count("{") - s.count("}") == 0 and s.count("[") - s.count("]") == 0:
        
        s = list(s)
        stack = list()
        
        while s:
            
            char = s.pop(0)
    
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            
            else:
                if stack and ((char == ")" and stack[-1] == "(") or (char == "}" and stack[-1] == "{") or (char == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False

        return True

    return False
        

print(function(s))