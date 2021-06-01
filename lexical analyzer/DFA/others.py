SYMBOL = ['~','@','#','$','%','^','&','*']
COMMA = [',']
PARENS = ['(',')','[',']','{','}']
WHITE_SPACE = [' ', '\t', '\n']
OTHERS = SYMBOL + COMMA + PARENS + WHITE_SPACE

def isOthers(token):
    state = ['T0', 'T1']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in OTHERS :
                locate = state[1]
            else : return False
        else : return False
    
    if locate == state[1]:
        return True
    else:
        return False

token = "("
result = isOthers(token)
print(result)