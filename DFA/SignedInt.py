ZERO = ['0']
NON_ZERO = ['1','2','3','4','5','6','7','8','9']
MINUS = ['-']

def isSignedINT(token) :
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in ZERO : 
                locate = state[1]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in MINUS : 
                locate = state[2]
            else : return False
        elif locate == state[2]:
            if value in NON_ZERO:
                locate = state[3]
            else : return False
        elif locate == state[3]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else : return False
        elif locate == state[4]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else : return False
        elif locate == state[5]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else : return False
    
    if locate == state[1] or locate == state[3] or locate == state[4] or locate == state[5]:
        return True
    else:
        return False



token = '0'
result = isSignedINT(token)
print(result)