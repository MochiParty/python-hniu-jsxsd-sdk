

def encoded(username: str, password: str, decoded: str) -> str:
    arr = decoded.split('#')
    scode = arr[0]
    sxh = arr[1]
    code = username+"%%%"+password
    encoded = ""
    for i in range(len(code)):
        if i < 20:
            encoded = encoded + code[i:i+1] + scode[0:int(sxh[i:i+1])]
            scode = scode[int(sxh[i:i+1]):len(scode)]
        else:
            encoded = encoded + code[i:len(code)]
            break
    return encoded

