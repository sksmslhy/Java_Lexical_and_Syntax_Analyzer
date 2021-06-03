import sys

# Command 내 인자 개수 확인
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

# 재귀 제한 설정
sys.setrecursionlimit(10000000)

# input File 열기
file_path = sys.argv[1]
f = open(file_path, 'r')


# define token & symbol
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
ZERO = ['0']
MINUS = ['-']
NON_ZERO = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
UNDER_BAR = ['_']
ARITHMETIC = ['+', '-', '*', '/']
COMPARISON = ['<', '>', '!', '=']
ASSIGN = ['=']
QUOTE = ["'"]
DOUBLE_QUOTE = ['"']
SYMBOL = ['~', '@', '#', '$', '%', '^', '&', '?', '!', '|', '\\', '.', ':']
COMMA = [',']
PARENS = ['(', ')', '[', ']', '{', '}']
SEMI = [';']
WHITE_SPACE = [' ', '\t', '\n']
LETTER = ALPHABET + SYMBOL
OTHERS = SYMBOL + COMMA + PARENS + WHITE_SPACE + SEMI + ASSIGN
VTYPE = ['int', 'char', 'boolean', 'String', 'void', 'byte', 'double', 'float',
         'long']
KEYWORD = ['if', 'else', 'while', 'return', 'class']


# DFA implementation
# Arithmetic인지 check
def isArithmetic(token):
    # state 정의
    state = ['T0', 'T1', 'T2', 'T3', 'T4']
    # 입력이 들어오면 현재 state를 start state로 지정한다.
    locate = state[0]
    # 입력받은 token을 하나하나 state의 입력으로 받는 것을 반복한다.
    for value in token:
        if locate == state[0]:
            if value in ARITHMETIC[0]:
                locate = state[1]
            elif value in ARITHMETIC[1]:
                locate = state[2]
            elif value in ARITHMETIC[2]:
                locate = state[3]
            elif value in ARITHMETIC[3]:
                locate = state[4]
            else:
                return False
        else:
            return False
    # 입력을 다 읽은 후 현재의 state가 Arithmetic DFA의 final state면 True를, 그렇지 않으면 False를 반환한다.
    if locate == state[1] or locate == state[2] or locate == state[3] or locate == state[4]:
        return True
    else:
        return False


def isComparison(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in COMPARISON[0]:
                locate = state[2]
            elif value in COMPARISON[1]:
                locate = state[1]
            elif value in COMPARISON[2]:
                locate = state[3]
            elif value in COMPARISON[3]:
                locate = state[4]
            else:
                return False
        elif locate == state[1]:
            if value in COMPARISON[3]:
                locate = state[5]
            else:
                return False
        elif locate == state[2]:
            if value in COMPARISON[3]:
                locate = state[5]
            else:
                return False
        elif locate == state[3]:
            if value in COMPARISON[3]:
                locate = state[5]
            else:
                return False
        elif locate == state[4]:
            if value in COMPARISON[3]:
                locate = state[5]
            else:
                return False
        else:
            return False
    if locate == state[1] or locate == state[2] or locate == state[5]:
        return True
    else:
        return False


def isID(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in ALPHABET:
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
            elif value in ALPHABET:
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
            elif value in ALPHABET:
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
            elif value in ALPHABET:
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
            elif value in ALPHABET:
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
            elif value in ALPHABET:
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
            elif value in ALPHABET:
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


def isLiteralString(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in DOUBLE_QUOTE:
                locate = state[1]
            else:
                return False
        elif locate == state[1]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            else:
                return False
        elif locate == state[2]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            elif value in DOUBLE_QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[3]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            elif value in DOUBLE_QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[4]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            elif value in DOUBLE_QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[5]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in LETTER:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            elif value in DOUBLE_QUOTE:
                locate = state[6]
            else:
                return False
        else:
            return False
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


def isSingleCharacter(token):
    state = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    locate = state[0]
    for value in token:
        if locate == state[0]:
            if value in QUOTE:
                locate = state[1]
            else:
                return False
        elif locate == state[1]:
            if value in ZERO:
                locate = state[2]
            elif value in NON_ZERO:
                locate = state[3]
            elif value in ALPHABET:
                locate = state[4]
            elif value in WHITE_SPACE:
                locate = state[5]
            else:
                return False
        elif locate == state[2]:
            if value in QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[3]:
            if value in QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[4]:
            if value in QUOTE:
                locate = state[6]
            else:
                return False
        elif locate == state[5]:
            if value in QUOTE:
                locate = state[6]
            else:
                return False
        else:
            return False

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


### Double Quote(")를 체크하여 List 내 Char를 결합해주는 함수
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
    # List 반환
    return result


### Single Quote(')를 체크하여 List 내 Char를 결합해주는 함수
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
    # List 반환
    return result


# Lexeme value를 저장하는 List 초기화
token_value = []

# Token 종류를 저장하는 List 초기화
token_key = []

# 입력 Stream을 저장한기 위한 문자열 초기화
initial_input = ''


### 입력 Stream을 받아 이를 Char 단위로 쪼개어 List 반환 ("", '' 처리 포함)
def preProcessing(input_str: str):
    # 전역 변수 사용
    global initial_input
    # 결과 출력을 위한 Stream 복사
    initial_input = input_str
    # String to List
    test = list(input_str)
    # "", '' 처리 수행
    test = checkDoubleQuote(checkSingleQuote(test))
    # List 반환
    return test


### 재귀 방식으로 작동하는 tokenize 함수, List를 입력받아 최초 토큰을 반환하고 나머지 List를 재귀 함수의 Input으로 활용
def tokenize(input_string: list):
    global token_value
    global token_key
    global initial_input

    # print('#### LOOP ########################################################')
    # print("input :", input_string)

    # 더 이상 분석할 String이 존재하지 않으면 tokenize 함수 반환
    if len(input_string) == 0:
        # print("-------------------------------------------------------------")
        # print("INPUT :", initial_input)
        # print("LEXEM :", token_value)
        # print("TOKEN :", token_key)
        return

    # 반복문을 통해 검사할 Char 리스트를 재구성
    # ex. 'abc1' -> [['a'], ['a','b'], ['a','b','c'], ['a','b','c','1']]
    while True:
        test_iter = []
        for i in range(len(input_string)):
            test_iter.append(input_string[0:i + 1])
        break
    # print(test_iter)

    # 모든 DFA에서 Reject 되기 전까지 Accept 되었던 횟수 Count
    # 이는 - 심볼 처리 혹은 다른 애매한 상황에 대한 판단 등에 쓰임
    count_Arith = 0
    count_Compa = 0
    count_ID = 0
    count_Liter = 0
    count_SiINT = 0
    count_SiChr = 0
    count_Other = 0

    # print('\tArith | Compa |  ID   | Liter | SiINT | SiChr | Other')
    # print('\t-----------------------------------------------------')

    # Lexeme, Token Insert을 위한 Temp value
    token = ''
    token_type = None

    # Char List Check Count
    count = 0

    # 재귀 방식의 Char List 반복 검사
    for i in test_iter:
        # 검사 횟수 Count
        count = count + 1

        # 현재 검사되는 Char List 조회를 위해 String 변환
        temp_str = ''.join(i)

        # 모든 DFA 검사에서 Reject되는 경우 반복문 break 후 다음 Char List 검사
        if ((isArithmetic(temp_str) == False)
                and (isComparison(temp_str) == False)
                and (isID(temp_str) == False)
                and (isLiteralString(temp_str) == False)
                and (isSignedINT(temp_str) == False)
                and (isSingleCharacter(temp_str) == False)
                and (isOthers(temp_str) == False)):
            # print("'"+temp_str+"'", ">>REJECT<<")
            # print("\tFalse | False | False | False | False | False | False")

            # Reject 직전의 Char까지 하여 Lexeme 구성
            token = ''.join(i[0:-1])

            # 다음 Input Stream 구성을 위해 Count - 1 수행
            count = count - 1

            break

        # print("'"+temp_str+"'")

        # Arithmetic DFA 검사
        if (isArithmetic(temp_str) == True):
            count_Arith = count_Arith + 1
            if temp_str in ['+', '-']:
                token_type = 'addsub'
            else:
                token_type = 'multdiv'
        # print("\t", isArithmetic(temp_str), end=' | ')

        # Comparision DFA 검사
        if (isComparison(temp_str) == True):
            count_Compa = count_Compa + 1
            token_type = 'comp'
        # print(isComparison(temp_str), end=' | ')

        # Identifier DFA 검사
        if (isID(temp_str) == True):
            count_ID = count_ID + 1

            # 사전에 지정된 예약어(Keyword)인 경우
            if temp_str in KEYWORD:
                if temp_str == 'if':
                    token_type = 'if'
                elif temp_str == 'else':
                    token_type = 'else'
                elif temp_str == 'while':
                    token_type = 'while'
                elif temp_str == 'return':
                    token_type = 'return'
                elif temp_str == 'class':
                    token_type = 'class'
                else:
                    token_type = 'KEYWORD'

            # 데이터 타입(Value Type)인 경우
            elif temp_str in VTYPE:
                if temp_str == 'boolean':
                    token_type = 'boolstr'
                else:
                    token_type = 'vtype'

            # 그 외의 경우 ID
            else:
                token_type = 'id'
        # print(isID(temp_str), end=' | ')

        # Literal String DFA 검사
        if (isLiteralString(temp_str) == True):
            count_Liter = count_Liter + 1
            token_type = 'literal'
        # print(isLiteralString(temp_str), end=' | ')

        # Signed Integer DFA 검사
        if (isSignedINT(temp_str) == True):
            count_SiINT = count_SiINT + 1
            token_type = 'num'
        # print(isSignedINT(temp_str), end=' | ')

        # Single Character DFA 검사
        if (isSingleCharacter(temp_str) == True):
            count_SiChr = count_SiChr + 1
            token_type = 'character'
        # print(isSingleCharacter(temp_str), end=' | ')

        # 그 외의 경우(Others)에 대한 DFA 검사
        if (isOthers(temp_str) == True):
            count_Others = count_Other + 1
            token_type = 'OTHERS'

            # Others는 기호(Symbol), 콤마(Comma), 괄호(Parens, ex.[]{}()), White Space, 세미콜론(Semi), 할당 연산자(Assign,=)으로 구성
            OTHERS = SYMBOL + COMMA + PARENS + WHITE_SPACE + SEMI + ASSIGN

            # 사전에 지정된 기호(Symbol)인 경우
            if temp_str in SYMBOL:
                token_type = 'SYMBOL'

            # 사전에 지정된 콤마(Comma)인 경우
            elif temp_str in COMMA:
                token_type = 'comma'

            # 사전에 지정된 괄호 종류(Parens)인 경우
            elif temp_str in PARENS:
                if temp_str == '(':
                    token_type = 'lparen'
                elif temp_str == ')':
                    token_type = 'rparen'
                elif temp_str == '{':
                    token_type = 'lbrace'
                elif temp_str == '}':
                    token_type = 'rbrace'
                else:
                    token_type = 'PARENS'

            # White Space(' ', '\n', '\t')의 경우
            elif temp_str in WHITE_SPACE:
                token_type = 'WHITE_SPACE'

            # 세미콜론(;)의 경우
            elif temp_str in SEMI:
                token_type = 'semi'

            # 할당 연산자(=)의 경우
            elif temp_str in ASSIGN:
                token_type = 'assign'
        # print(isOthers(temp_str))

        # 각 Char List의 마지막 검사의 경우
        if (test_iter.index(i) == len(test_iter) - 1) and (True in [isArithmetic(temp_str),
                                                                    isComparison(temp_str),
                                                                    isID(temp_str),
                                                                    isLiteralString(temp_str),
                                                                    isSignedINT(temp_str),
                                                                    isSingleCharacter(temp_str),
                                                                    isOthers(temp_str)]):

            try:
                # (-) Symbol 처리, 연산자가 될 것인지, Integer 처리할 것인지 결정
                if (count_Arith >= 1) and (count_SiINT >= 1) and (token_key[-1] in ['INT', 'ID']):
                    # -- Arithmatic DFA Accept 횟수와 Signed Interger DFA Accept 횟수가 모두 1 이상이고,
                    # -- 바로 직전 Token이 Int 혹은 ID일 경우 연산자 처리
                    token = temp_str[0]
                    token_type = 'ARITHMETIC'
                else:
                    token = temp_str

            # (-) Symbol이 Input의 맨 앞에 나온 경우 Out of List range 예외 처리
            except:
                token = temp_str

        # print("\t", '---------------------------------------------')

    # 모든 DFA 검사에서 Reject되어 Lexeme 분류가 이루어지지 않은 경우
    if token == "":
        token = "NO TOKEN"

    # print("\t%5d   %5d   %5d   %5d   %5d   %5d   %5d" %(count_Arith, count_Compa, count_ID,
    # count_Liter, count_SiINT, count_SiChr, count_Other))

    # print("\nInput :", "'"+''.join(input_string)+"'")
    # print("Output :", "'"+token+"'")

    # 재귀 함수의 Input이 될 새로운 Input String List를 결정
    try:
        if (count_Arith >= 1) and (count_SiINT >= 1) and (token_key[-1] in ['INT', 'ID']):
            token = temp_str[0]
            token_type = 'ARITHMETIC'

            new_test = input_string[1:]

        else:
            new_test = input_string[count:]

    # (-) Symbol이 Input의 맨 앞에 나온 경우 Out of List range 예외 처리
    except:
        new_test = input_string[count:]

    # print("FINDME", input_string)

    # 결정된 Lexeme을 전역 변수로 선언된 List에 삽입
    token_value.append(token)

    # 결정된 Token Type을 전역 변수로 선언된 List에 삽입
    token_key.append(token_type)

    # 재귀 방식으로 나머지 Input String에 대한 Tokenize 계속 실행
    tokenize(new_test)


### 결과를 새로운 파일에 출력 및 저장하는 함수
def save_result():
    global token_value
    global token_key
    # Output File에 대한 이름은 '<input_file_name>_output.txt'로 저장됨
    save = open(file_path + '_output.txt', 'w')
    for i, j in zip(token_value, token_key):
        # White Space를 제외하고 저장
        if j != 'WHITE_SPACE':
            #save.write("<" + j + ", " + i + ">\n")
            save.write(j + "\n")
            # print("<"+j+",", i+">")
    print("Successfully token list saved")
    save.close


### 전체 Lexical Analyzer Flow에 대한 Process 실행
def process(input_str: str):
    global token_value
    global token_key
    token_value = []
    token_key = []
    initial_input = ''
    # PreProcessing
    test = preProcessing(input_str)
    # Tokenize
    tokenize(test)
    # Save Result
    save_result()


# Command에서 받은 Code에 대한 Lexical Analize Process 호출
process(f.read())

