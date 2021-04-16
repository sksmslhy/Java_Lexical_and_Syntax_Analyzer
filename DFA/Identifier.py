LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ZERO = ['0']
NON_ZERO = ['1','2','3','4','5','6','7','8','9']
UNDER_BAR = ['_']


def isID(token):  
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in LETTER : 
                locate = state[1]
            elif value in UNDER_BAR : 
                locate = state[2]
            else : return False
        elif locate == state[1] :
            if value in ZERO : 
                locate = state[3]
            elif value in NON_ZERO :
                locate = state[4]
            elif value in LETTER : 
                locate = state[5]
            elif value in UNDER_BAR : 
                locate = state[6]
            else : return False
        elif locate == state[2] :
            if value in ZERO : 
                locate = state[3]
            elif value in NON_ZERO :
                locate = state[4]
            elif value in LETTER : 
                locate = state[5]
            elif value in UNDER_BAR : 
                locate = state[6]
            else : return False
         
    if locate == state[1] or locate == state[2] or locate == state[3] or locate == state[4] or locate == state[5] or locate == state[6]:
        return True
    else:
        return False


token = 'this_is_ID'
result = isID(token)
print(result)