COMPARISON = ['<', '>', '!', '=']

def isComparison(token):  
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in COMPARISON[0] : 
                locate = state[2]
            elif value in COMPARISON[1] : 
                locate = state[1]
            elif value in COMPARISON[2] : 
                locate = state[3]
            elif value in COMPARISON[3] : 
                locate = state[4]
            else : return False
        elif locate == state [1] : 
            if value in COMPARISON[3] : 
                locate = state[5]
            else : return False
        elif locate == state [2] : 
            if value in COMPARISON[3] : 
                locate = state[5]
            else : return False
        elif locate == state [3] : 
            if value in COMPARISON[3] : 
                locate = state[5]
            else : return False
        elif locate == state [4] : 
            if value in COMPARISON[3] : 
                locate = state[5]
            else : return False
    if locate == state[1] or locate == state[2] or locate == state[5]:
        return True
    else:
        return False


token = '>='
result = isComparison(token)
print(result)