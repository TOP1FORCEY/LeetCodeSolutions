s = "MCMXCIV"

output = 0
        
symbols = [sym for sym in s]

while symbols:

    symbol = symbols.pop(0)

    if symbol == "I":
        output += 1 
        if symbols:
            if symbols[0] == "V":
                output += 3
                symbols.pop(0)
            elif symbols[0] == "X":
                output += 8
                symbols.pop(0)
        
    if symbol == "V":
        output += 5
    
    if symbol == "X":
        output += 10
        if symbols:
            if symbols[0] == "L":
                output += 30
                symbols.pop(0)
            elif symbols[0] == "C":
                output += 80
                symbols.pop(0)
        
    if symbol == "L":
        output += 50
    
    if symbol == "C":
        output += 100
        if symbols:
            if symbols[0] == "D":
                output += 300
                symbols.pop(0)
            elif symbols[0] == "M":
                output += 800
                symbols.pop(0)
        
    if symbol == "D":
        output += 500
    
    if symbol == "M":
        output += 1000
    
    print(output)

    


        
    