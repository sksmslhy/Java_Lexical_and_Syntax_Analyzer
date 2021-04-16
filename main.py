LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ZERO = ['0']
MINUS = ['-']
NON_ZERO = ['1','2','3','4','5','6','7','8','9']
UNDER_BAR = ['_']
ARITHMETIC = ['+','-','*','/']
COMPARISON = ['<', '>', '!', '=']
ASSIGN = ['=']
QUOTE = ["'"]
DOUBLE_QUOTE = ['"']
SYMBOL = ['~','@','#','$','%','^','&','*']
COMMA = [',']
PARENS = ['(',')','[',']','{','}']
SEMI = [';']
WHITE_SPACE = [' ', '\t', '\n']
OTHERS = SYMBOL + COMMA + PARENS + WHITE_SPACE + SEMI + ASSIGN
VTYPE = ['int','char','boolean','String', 'void', 'byte', 'double', 'float',
        'long']
KEYWORD = ['abstract', 'break', 'case', 'catch', 'class', 'continue', 'default',
           'do', 'else', 'extends', 'false', 'finally', 'for', 'if', 'implements',
           'import', 'instanceof', 'interface', 'native', 'new', 'null', 'package',
           'private', 'protected', 'public', 'return', 'short', 'static', 'super',
           'switch', 'synchronized', 'this', 'throw', 'throws', 'true', 'try', 'while', 'args', 'main']

def isArithmetic(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in ARITHMETIC[0] :
                locate = state[1]
            elif value in ARITHMETIC[1] :
                locate = state[2]
            elif value in ARITHMETIC[2] :
                locate = state[3]
            elif value in ARITHMETIC[3] :
                locate = state[4]
            else : return False
        else : return False

    if locate == state[1] or locate == state[2] or locate == state[3] or locate == state[4]:
        return True
    else:
        return False

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
        else : return False
    if locate == state[1] or locate == state[2] or locate == state[5]:
        return True
    else:
        return False


def isID(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in LETTER:
                locate = state[2]
            elif value in UNDER_BAR:
                locate = state[1]
            else:
                return False
        elif locate == state[1]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        elif locate == state[2]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        elif locate == state[3]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        elif locate == state[4]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        elif locate == state[5]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        elif locate == state[6]:
            if value in ZERO:
                locate = state[3]
            elif value in NON_ZERO:
                locate = state[4]
            elif value in LETTER:
                locate = state[5]
            elif value in UNDER_BAR:
                locate = state[6]
            else:
                return False
        else:
            return False

    if locate == state[1] or locate == state[2] or locate == state[3] or locate == state[4] or locate == state[
        5] or locate == state[6]:
        return True
    else:
        return False

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
        else : return False
    if locate == state[6]:
        return True
    else:
        return False


def isSignedINT(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in ZERO:
                locate = state[1]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in MINUS:
                locate = state[2]
            else:
                return False
        elif locate == state[2]:
            if value in NON_ZERO:
                locate = state[3]
            else:
                return False
        elif locate == state[3]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else:
                return False
        elif locate == state[4]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else:
                return False
        elif locate == state[5]:
            if value in ZERO:
                locate = state[4]
            elif value in NON_ZERO:
                locate = state[5]
            else:
                return False
        else:
            return False

    if locate == state[1] or locate == state[3] or locate == state[4] or locate == state[5]:
        return True
    else:
        return False

def isSingleCharacter(token) :
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in QUOTE:
                locate = state[1]
            else : return False
        elif locate == state[1]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            else : return False
        elif locate == state[2]:
            if value in QUOTE:
                locate = state[6]
            else : return False
        elif locate == state[3]:
            if value in QUOTE:
                locate = state[6]
            else : return False
        elif locate == state[4]:
            if value in QUOTE:
                locate = state[6]
            else : return False
        elif locate == state[5]:
            if value in QUOTE:
                locate = state[6]
            else : return False
        else: return False

    if locate == state[6]:
        return True
    else:
        return False


def isOthers(token):
    state = ['T0', 'T1']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in OTHERS:
                locate = state[1]
            else:
                return False
        else:
            return False

    if locate == state[1]:
        return True
    else:
        return False


def checkDoubleQuote(string_list: list):
    result = []
    temp = []
    checkOn = False
    for i in string_list:
        if i == '"':
            if checkOn == True:
                temp.append('"')
                result.append(''.join(temp))
                temp = []
                checkOn = False
            elif checkOn == False:
                checkOn = True
                temp.append('"')
        else:
            if checkOn == False:
                result.append(i)
            elif checkOn == True:
                temp.append(i)
    return result


def checkSingleQuote(string_list: list):
    result = []
    temp = []
    checkOn = False
    for i in string_list:
        if i == "'":
            if checkOn == True:
                temp.append("'")
                result.append(''.join(temp))
                temp = []
                checkOn = False
            elif checkOn == False:
                checkOn = True
                temp.append("'")
        else:
            if checkOn == False:
                result.append(i)
            elif checkOn == True:
                temp.append(i)
    return result


token_value = []
token_key = []
initial_input = ''


def preProcessing(input_str: str):
    global initial_input
    initial_input = input_str
    test = list(input_str)
    test = checkDoubleQuote(checkSingleQuote(test))
    return test


def tokenize(input_string: list):
    global token_value
    global token_key
    global initial_input
    # print('#### LOOP ########################################################')
    # print("input :", input_string)
    if len(input_string) == 0:
        # print("-------------------------------------------------------------")
        # print("INPUT :", initial_input)
        # print("LEXEM :", token_value)
        # print("TOKEN :", token_key)
        return

    while True:
        test_iter = []
        for i in range(len(input_string)):
            test_iter.append(input_string[0:i + 1])
        break
    # print(test_iter)
    count_Arith = 0
    count_Compa = 0
    count_ID = 0
    count_Liter = 0
    count_SiINT = 0
    count_SiChr = 0
    count_Other = 0

    # print('\tArith | Compa |  ID   | Liter | SiINT | SiChr | Other')
    # print('\t-----------------------------------------------------')

    token = ''
    count = 0
    token_type = None
    for i in test_iter:
        count = count + 1
        temp_str = ''.join(i)

        if ((isArithmetic(temp_str) == False)
                and (isComparison(temp_str) == False)
                and (isID(temp_str) == False)
                and (isLiteralString(temp_str) == False)
                and (isSignedINT(temp_str) == False)
                and (isSingleCharacter(temp_str) == False)
                and (isOthers(temp_str) == False)):
            # print("'"+temp_str+"'", ">>REJECT<<")
            # print("\tFalse | False | False | False | False | False | False")
            token = ''.join(i[0:-1])
            count = count - 1
            break

        # print("'"+temp_str+"'")

        # print("\t", isArithmetic(temp_str), end=' | ')
        if (isArithmetic(temp_str) == True):
            count_Arith = count_Arith + 1
            token_type = 'ARITHMETIC'

        # print(isComparison(temp_str), end=' | ')
        if (isComparison(temp_str) == True):
            count_Compa = count_Compa + 1
            token_type = 'COMPARISON'

        # print(isID(temp_str), end=' | ')
        if (isID(temp_str) == True):
            count_ID = count_ID + 1
            if temp_str in KEYWORD:
                token_type = 'KEYWORD'
            elif temp_str in VTYPE:
                token_type = 'VTYPE'
            else:
                token_type = 'ID'

        # print(isLiteralString(temp_str), end=' | ')
        if (isLiteralString(temp_str) == True):
            count_Liter = count_Liter + 1
            token_type = 'LITERAL'

        # print(isSignedINT(temp_str), end=' | ')
        if (isSignedINT(temp_str) == True):
            count_SiINT = count_SiINT + 1
            token_type = 'INT'

        # print(isSingleCharacter(temp_str), end=' | ')
        if (isSingleCharacter(temp_str) == True):
            count_SiChr = count_SiChr + 1
            token_type = 'CHAR'

        # print(isOthers(temp_str))
        if (isOthers(temp_str) == True):
            count_Others = count_Other + 1
            token_type = 'OTHERS'
            OTHERS = SYMBOL + COMMA + PARENS + WHITE_SPACE + SEMI + ASSIGN
            if temp_str in SYMBOL:
                token_type = 'SYMBOR'
            elif temp_str in COMMA:
                token_type = 'COMMA'
            elif temp_str in PARENS:
                token_type = 'PARENS'
            elif temp_str in WHITE_SPACE:
                token_type = 'WHITE_SPACE'
            elif temp_str in SEMI:
                token_type = 'SEMI'
            elif temp_str in ASSIGN:
                token_type = 'ASSIGN'

        if (test_iter.index(i) == len(test_iter) - 1) and (True in [isArithmetic(temp_str),
                                                                    isComparison(temp_str),
                                                                    isID(temp_str),
                                                                    isLiteralString(temp_str),
                                                                    isSignedINT(temp_str),
                                                                    isSingleCharacter(temp_str),
                                                                    isOthers(temp_str)]):
            if (count_Arith >= 1) and (count_SiINT >= 1) and (token_key[-1] in ['INT', 'ID']):
                token = temp_str[0]
                token_type = 'ARITHMETIC'
            else:
                token = temp_str

        # print("\t", '---------------------------------------------')

    # print("\t%5d   %5d   %5d   %5d   %5d   %5d   %5d" %(count_Arith, count_Compa, count_ID,
    # count_Liter, count_SiINT, count_SiChr, count_Other))

    # print("\nInput :", "'"+''.join(input_string)+"'")

    if token == "":
        token = "NO TOKEN"
    # print("Output :", "'"+token+"'")

    if (count_Arith >= 1) and (count_SiINT >= 1) and (token_key[-1] in ['INT', 'ID']):
        token_value.append(token)
        token_key.append(token_type)
        new_test = input_string[1:]
        tokenize(new_test)
    else:
        token_value.append(token)
        token_key.append(token_type)
        new_test = input_string[count:]
        tokenize(new_test)


def print_result():
    global token_value
    global token_key
    for i, j in zip(token_value, token_key):
        if j != 'WHITE_SPACE':
            print("<" + j + ",", i + ">")


def process(input_str: str):
    global token_value
    global token_key
    token_value = []
    token_key = []
    initial_input = ''
    test = preProcessing(input_str)
    tokenize(test)
    print_result()

process("HI 123")