import copy
import sys

RULE = [
    ['S', 'CODE'],
    ['CODE', 'VDECL CODE'],
    ['CODE', 'FDECL CODE'],
    ['CODE', 'CDECL CODE'],
    ['CODE', 'epsilon'],
    ['VDECL', 'vtype id semi'],
    ['VDECL', 'vtype ASSIGN semi'],
    ['ASSIGN', 'id assign RHS'],
    ['RHS', 'EXPR'],
    ['RHS', 'literal'],
    ['RHS', 'character'],
    ['RHS', 'boolstr'],
    ['EXPR', 'TERM addsub EXPR'],
    ['EXPR', 'TERM'],
    ['TERM', 'FACTOR multdiv TERM'],
    ['TERM', 'FACTOR'],
    ['FACTOR', 'lparen EXPR rparen'],
    ['FACTOR', 'id'],
    ['FACTOR', 'num'],
    ['FDECL', 'vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace'],
    ['ARG', 'vtype id MOREARGS'],
    ['ARG', 'epsilon'],
    ['MOREARGS', 'comma vtype id MOREARGS'],
    ['MOREARGS', 'epsilon'],
    ['BLOCK', 'STMT BLOCK'],
    ['BLOCK', 'epsilon'],
    ['STMT', 'VDECL'],
    ['STMT', 'ASSIGN semi'],
    ['STMT', 'if lparen COND rparen lbrace BLOCK rbrace ELSE'],
    ['STMT', 'while lparen COND rparen lbrace BLOCK rbrace'],
    ['COND', 'FACTOR comp FACTOR'],
    ['COND', 'boolstr'],
    ['ELSE', 'else lbrace BLOCK rbrace'],
    ["ELSE', 'epsilon"],
    ['RETURN', 'return RHS semi'],
    ['CDECL', 'class id lbrace ODECL rbrace'],
    ['ODECL', 'VDECL ODECL'],
    ['ODECL', 'FDECL ODECL'],
    ['ODECL', 'epsilon']

]

SLR_TABLE = [
    {'vtype': 'S5', 'class': 'S6', '$': 'R4', 'CODE': 1, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4, },
    {'$': 'ACC', },
    {'vtype': 'S5', 'class': 'S6', '$': 'R4', 'CODE': 7, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4, },
    {'vtype': 'S5', 'class': 'S6', '$': 'R4', 'CODE': 8, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4, },
    {'vtype': 'S5', 'class': 'S6', '$': 'R4', 'CODE': 9, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4, },
    {'id': 'S10', 'ASSIGN': 11, },
    {'id': 'S12', },
    {'$': 'R1', },
    {'$': 'R2', },
    {'$': 'R3', },
    {'semi': 'S13', 'assign': 'S15', 'lparen': 'S14', },
    {'semi': 'S16', },
    {'lbrace': 'S17', },
    {'vtype': 'R5', 'id': 'R5', 'rbrace': 'R5', 'if': 'R5', 'while': 'R5', 'return': 'R5', 'class': 'R5', '$': 'R5', },
    {'vtype': 'S19', 'rparen': 'R21', 'ARG': 18, },
    {'id': 'S28', 'literal': 'S22', 'character': 'S23', 'boolstr': 'S24', 'lparen': 'S27', 'num': 'S29', 'RHS': 20,
     'EXPR': 21, 'TERM': 25, 'FACTOR': 26, },
    {'vtype': 'R6', 'id': 'R6', 'rbrace': 'R6', 'if': 'R6', 'while': 'R6', 'return': 'R6', 'class': 'R6', '$': 'R6', },
    {'vtype': 'S5', 'rbrace': 'R38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 30, },
    {'rparen': 'S33', },
    {'id': 'S34', },
    {'semi': 'R7', },
    {'semi': 'R8', },
    {'semi': 'R9', },
    {'semi': 'R10', },
    {'semi': 'R11', },
    {'semi': 'R13', 'addsub': 'S35', 'rparen': 'R13', },
    {'semi': 'R15', 'addsub': 'R15', 'multdiv': 'S36', 'rparen': 'R15', },
    {'id': 'S28', 'lparen': 'S27', 'num': 'S29', 'EXPR': 37, 'TERM': 25, 'FACTOR': 26, },
    {'semi': 'R17', 'addsub': 'R17', 'multdiv': 'R17', 'rparen': 'R17', 'comp': 'R17', },
    {'semi': 'R18', 'addsub': 'R18', 'multdiv': 'R18', 'rparen': 'R18', 'comp': 'R18', },
    {'rbrace': 'S38', },
    {'vtype': 'S5', 'rbrace': 'R38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 39, },
    {'vtype': 'S5', 'rbrace': 'R38', 'VDECL': 31, 'FDECL': 32, 'ODECL': 40, },
    {'lbrace': 'S41', },
    {'rparen': 'R23', 'comma': 'S43', 'MOREARGS': 42, },
    {'id': 'S28', 'lparen': 'S27', 'num': 'S29', 'EXPR': 44, 'TERM': 25, 'FACTOR': 26, },
    {'id': 'S28', 'lparen': 'S27', 'num': 'S29', 'TERM': 45, 'FACTOR': 26, },
    {'rparen': 'S46', },
    {'vtype': 'R35', 'class': 'R35', '$': 'R35', },
    {'rbrace': 'R36', },
    {'rbrace': 'R37', },
    {'vtype': 'S53', 'id': 'S54', 'rbrace': 'R25', 'if': 'S51', 'while': 'S52', 'return': 'R25', 'VDECL': 49,
     'ASSIGN': 50, 'BLOCK': 47, 'STMT': 48, },
    {'rparen': 'R20', },
    {'vtype': 'S55', },
    {'semi': 'R12', 'rparen': 'R12', },
    {'semi': 'R14', 'addsub': 'R14', 'rparen': 'R14', },
    {'semi': 'R16', 'addsub': 'R16', 'multdiv': 'R16', 'rparen': 'R16', 'comp': 'R16', },
    {'return': 'S57', 'RETURN': 56, },
    {'vtype': 'S53', 'id': 'S54', 'rbrace': 'R25', 'if': 'S51', 'while': 'S52', 'return': 'R25', 'VDECL': 49,
     'ASSIGN': 50, 'BLOCK': 58, 'STMT': 48, },
    {'vtype': 'R26', 'id': 'R26', 'rbrace': 'R26', 'if': 'R26', 'while': 'R26', 'return': 'R26', },
    {'semi': 'S59', },
    {'lparen': 'S60', },
    {'lparen': 'S61', },
    {'id': 'S62', 'ASSIGN': 11, },
    {'assign': 'S15', },
    {'id': 'S63', },
    {'rbrace': 'S64', },
    {'id': 'S28', 'literal': 'S22', 'character': 'S23', 'boolstr': 'S24', 'lparen': 'S27', 'num': 'S29', 'RHS': 65,
     'EXPR': 21, 'TERM': 25, 'FACTOR': 26, },
    {'rbrace': 'R24', 'return': 'R24', },
    {'vtype': 'R27', 'id': 'R27', 'rbrace': 'R27', 'if': 'R27', 'while': 'R27', 'return': 'R27', },
    {'id': 'S28', 'boolstr': 'S68', 'lparen': 'S27', 'num': 'S29', 'FACTOR': 67, 'COND': 66, },
    {'id': 'S28', 'boolstr': 'S68', 'lparen': 'S27', 'num': 'S29', 'FACTOR': 67, 'COND': 69, },
    {'semi': 'S13', 'assign': 'S15', },
    {'rparen': 'R23', 'comma': 'S43', 'MOREARGS': 70, },
    {'vtype': 'R19', 'rbrace': 'R19', 'class': 'R19', '$': 'R19', },
    {'semi': 'S71', },
    {'rparen': 'S72', },
    {'comp': 'S73', },
    {'rparen': 'R31', },
    {'rparen': 'S74', },
    {'rparen': 'R22', },
    {'rbrace': 'R34', },
    {'lbrace': 'S75', },
    {'id': 'S28', 'lparen': 'S27', 'num': 'S29', 'FACTOR': 76, },
    {'lbrace': 'S77', },
    {'vtype': 'S53', 'id': 'S54', 'rbrace': 'R25', 'if': 'S51', 'while': 'S52', 'return': 'R25', 'VDECL': 49,
     'ASSIGN': 50, 'BLOCK': 78, 'STMT': 48, },
    {'rparen': 'R30', },
    {'vtype': 'S53', 'id': 'S54', 'rbrace': 'R25', 'if': 'S51', 'while': 'S52', 'return': 'R25', 'VDECL': 49,
     'ASSIGN': 50, 'BLOCK': 79, 'STMT': 48, },
    {'rbrace': 'S80', },
    {'rbrace': 'S81', },
    {'vtype': 'R33', 'id': 'R33', 'rbrace': 'R33', 'if': 'R33', 'while': 'R33', 'else': 'S83', 'return': 'R33',
     'ELSE': 82, },
    {'vtype': 'R29', 'id': 'R29', 'rbrace': 'R29', 'if': 'R29', 'while': 'R29', 'return': 'R29', },
    {'vtype': 'R28', 'id': 'R28', 'rbrace': 'R28', 'if': 'R28', 'while': 'R28', 'return': 'R28', },
    {'lbrace': 'S84', },
    {'vtype': 'S53', 'id': 'S54', 'rbrace': 'R25', 'if': 'S51', 'while': 'S52', 'return': 'R25', 'VDECL': 49,
     'ASSIGN': 50, 'BLOCK': 85, 'STMT': 48, },
    {'rbrace': 'S86', },
    {'vtype': 'R32', 'id': 'R32', 'rbrace': 'R32', 'if': 'R32', 'while': 'R32', 'return': 'R32', },
    ]


# this is for debugging
def print_terminal_list(terminal_list: list, splitter: int):
    temp = ""
    for i in range(0, splitter):
        temp += terminal_list[i] + " "
    temp += "|%d| " % splitter
    for i in range(splitter, len(terminal_list)):
        temp += terminal_list[i] + " "
    return temp


def parser():
    if len(terminal_list) == 1:
        return True, ''

    SLR_stack = [0]
    splitter = 0
    error_line = 1
    check = 0

    while True:
        next_input_symbol = terminal_list[splitter]
        check += 1
        current_state = SLR_stack[-1]

        if current_state == 1 and next_input_symbol == '$':
            print("ACCEPTED!!!")
            return True

        # 판단할 수 없는 symbol이 있으면 error
        if next_input_symbol not in SLR_TABLE[current_state].keys():
            error = "[REJECTED] Error in line " + str(error_line) + ", " + error_checker[error_line-1]
            print(error)
            return False, error

        # shift
        if SLR_TABLE[current_state][next_input_symbol][0] == 'S':
            splitter += 1
            error_line += 1
            SLR_stack.append(int(SLR_TABLE[current_state][next_input_symbol][1:]))

        # Reduce
        elif SLR_TABLE[current_state][next_input_symbol][0] == 'R':
            table_num = SLR_TABLE[current_state][next_input_symbol][1:]

            non_termi = RULE[int(table_num)][0]  # ex) CODE → epsilon 에서 VDECL 의미
            termi = RULE[int(table_num)][1]  # ex) CODE → epsilon 에서 epsilon 의미
            termi_length = len(str(termi).split(" "))  # 룰의 어절의 개수  ex) VDECL → vtype id semi : 3

            for i in range(termi_length):
                if termi != 'epsilon':
                    SLR_stack.pop()
                    terminal_list.pop(splitter-i-1)

            if non_termi not in SLR_TABLE[SLR_stack[-1]].keys():
                error = "[REJECTED] Error in line " + str(error_line) + ", " + error_checker[error_line - 1]
                print(error)
                return False, error

            # GOTO
            SLR_stack.append(SLR_TABLE[SLR_stack[-1]][non_termi])

            if termi != 'epsilon':
                splitter = splitter - termi_length + 1
            else:
                splitter += 1

            terminal_list.insert(splitter-1, non_termi)


# Command 내 인자 개수 확인
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

# input File 열기
file_path = sys.argv[1]
f = open(file_path, 'r')

END_MARK = '$'
terminal_list = []

lines = f.readlines()
for line in lines:
    terminal = line.split()[0]
    terminal_list.append(terminal)

terminal_list.append(END_MARK)
error_checker = copy.copy(terminal_list)

parser()
