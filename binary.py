a = "1010"
b = "1011"

def addBinary(a = list, b = list):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    
    if a:
        a = a[::-1]
        out_a = 0
        for i in range(len(a)):
            if a[i] == "1":
                out_a = out_a + (2 ** i)
    
    if b:
        b = b[::-1]   
        out_b = 0
        for i in range(len(b)):
            if b[i] == "1":
                out_b = out_b + (2 ** i)

    out = out_a + out_b
    res = ''

    if out == 0:
        return "0"

    while out > 0:
        print(res, out, bin(out)[2:])
        res = str(out & 1) + res
        out >>= 1

    return res

print(addBinary(a, b))