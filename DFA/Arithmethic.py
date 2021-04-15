ARITHMETIC = ['+','-','*','/']

def isArithmetic(token):  
    state = ['T0', 'T1', 'T2', 'T3', 'T4']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in ARITHMETIC[0] : 
                locate = state[1]
            elif vlaue in ARITHMETIC[1] : 
                locate = state[2]
            elif vlaue in ARITHMETIC[2] : 
                locate = state[3]
            elif vlaue in ARITHMETIC[3] : 
                locate = state[4]
            else : return False

    if locate == state[1] or locate == state[2] or locate == state[3] or locate == state[4]:
        return True
    else:
        return False


token = '+'
result = isArithmetic(token)
print(result)