LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ZERO = ['0']
NON_ZERO = ['1','2','3','4','5','6','7','8','9']
WHITE_SPACE = [' ', '\t', '\n', '']
DOUBLE_QUOTE = ['"']

def isLiteralString(token) :
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in DOUBLE_QUOTE : 
                locate = state[1]
            else : return False
        elif locate == state[1] :
            if value in ZERO : 
                locate = state[2]
            elif value in NON_ZERO :
                locate = state[3]
            elif value in LETTER : 
                locate = state[4]
            elif value in WHITE_SPACE : 
                locate = state[5]
            else : return False
        elif locate == state[2] :
            if value in ZERO : 
                locate = state[2]
            elif value in NON_ZERO :
                locate = state[3]
            elif value in LETTER : 
                locate = state[4]
            elif value in WHITE_SPACE : 
                locate = state[5]
            elif value in DOUBLE_QUOTE : 
                locate = state[6]
            else : return False
        elif locate == state[3] :
            if value in ZERO : 
                locate = state[2]
            elif value in NON_ZERO :
                locate = state[3]
            elif value in LETTER : 
                locate = state[4]
            elif value in WHITE_SPACE : 
                locate = state[5]
            elif value in DOUBLE_QUOTE : 
                locate = state[6]
            else : return False
        elif locate == state[4] :
            if value in ZERO : 
                locate = state[2]
            elif value in NON_ZERO :
                locate = state[3]
            elif value in LETTER : 
                locate = state[4]
            elif value in WHITE_SPACE : 
                locate = state[5]
            elif value in DOUBLE_QUOTE : 
                locate = state[6]
            else : return False
        elif locate == state[5] :
            if value in ZERO : 
                locate = state[2]
            elif value in NON_ZERO :
                locate = state[3]
            elif value in LETTER : 
                locate = state[4]
            elif value in WHITE_SPACE : 
                locate = state[5]
            elif value in DOUBLE_QUOTE : 
                locate = state[6]
            else : return False
         
    if locate == state[6]:
        return True
    else:
        return False



token = '"literal String"'
result = isLiteralString(token)
print(result)