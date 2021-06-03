import copy
import re
import sys

# Command 내 인자 개수 확인
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

# input File 열기
file_path = sys.argv[1]
f = open(file_path, 'r')


RULE = [
    {'CODE': 'VDECL CODE'},
    {'CODE': 'FDECL CODE'},
    {'CODE': 'CDECL CODE'},
    {'CODE': 'epsilon'},
    {'VDECL': 'vtype id semi'},
    {'VDECL': 'vtype ASSIGN semi'},
    {'ASSIGN': 'id assign RHS'},
    {'RHS': 'EXPR'},
    {'RHS': 'literal'},
    {'RHS': 'character'},
    {'RHS': 'boolstr'},
    {'EXPR': 'TERM addsub EXPR'},
    {'EXPR': 'TERM'},
    {'TERM': 'FACTOR multdiv TERM'},
    {'TERM': 'FACTOR'},
    {'FACTOR': 'lparen EXPR rparen'},
    {'FACTOR': 'id'},
    {'FACTOR': 'num'},
    {'FDECL': 'vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace'},
    {'ARG': 'vtype id MOREARGS'},
    {"ARG': 'epsilon"},
    {'MOREARGS': 'comma vtype id MOREARGS'},
    {"MOREARGS': '''"},
    {'BLOCK': 'STMT BLOCK'},
    {"BLOCK': 'epsilon"},
    {'STMT': 'VDECL'},
    {'STMT': 'ASSIGN semi'},
    {'STMT': 'if lparen COND rparen lbrace BLOCK rbrace ELSE'},
    {'STMT': 'while lparen COND rparen lbrace BLOCK rbrace'},
    {'COND': 'FACTOR comp FACTOR'},
    {'COND': 'boolstr'},
    {'ELSE': 'else lbrace BLOCK rbrace'},
    {"ELSE': 'epsilon"},
    {'RETURN': 'return RHS semi'},
    {'CDECL': 'class id lbrace ODECL rbrace'},
    {'ODECL': 'VDECL ODECL'},
    {'ODECL': 'FDECL ODECL'},
    {"ODECL': 'epsilon"}
]

SLR_TABLE = [
    {'vtype': 'S2', 'VDECL': 1},
    {'vtype': 'S6', 'class': 'S7', '$': 'R3', 'CODE': 3, 'VDECL': 1, 'FDECL': 4, 'CDECL': 5},
    {'id': 'S8', 'ASSIGN': 9},
    {'$': 'ACC'},
    {'vtype': 'S6', 'class': 'S7', '$': 'R3', 'CODE': 10, 'VDECL': 1, 'FDECL': 4, 'CDECL': 5},
    {'vtype': 'S6', 'class': 'S7', '$': 'R3', 'CODE': 11, 'VDECL': 1, 'FDECL': 4, 'CDECL': 5},
    {'id': 'S12', 'ASSIGN': 9},
    {'id': 'S13'},
    {'semi': 'S14', 'assign': 'S15'},
    {'semi': 'S16'},
    {'$': 'R1'},
    {'$': 'R2'},
    {'semi': 'S14', 'assign': 'S15', 'lparen': 'S17'},
    {'rbrace': 'S18'},
    {'vtype': 'R4', 'id': 'R4', 'rbrace': 'R4', 'if': 'R4', 'while': 'R4', 'return': 'R4', 'class': 'R4', '$': 'R4'},
    {'id': 'S27', 'literal': 'S21', 'character': 'S22', 'boolstr': 'S23', 'lparen': 'S26', 'num': 'S28', 'RHS': 19, 'EXPR': 20, 'TERM': 24, 'FACTOR': 25}, # 15
    {'vtype': 'R5', 'id': 'R5', 'rbrace': 'R5', 'if': 'R5', 'while': 'R5', 'return': 'R5', 'class': 'R5', '$': 'R5'},
    {'vtype': 'S30', 'rparen': 'R20', 'ARG': 29},
    {'vtype': 'S6', 'rbrace': 'R37', 'VDECL': 32, 'FDECL': 33, 'ODECL': 31},
    {'semi': 'R6'},
    {'semi': 'R7'},
    {'semi': 'R8'},  # 20
    {'semi': 'R9'},
    {'semi': 'R10'},
    {'semi': 'R12', 'addsub': 'S34', 'rparen': 'R12'},
    {'semi': 'R14', 'addsub': 'R14', 'multdiv': 'S35', 'rparen': 'R14'},  # 25
    {'id': 'S27', 'lparen': 'S26', 'num': 'S28', 'EXPR': 36, 'TERM': 24, 'FACTOR': 25},
    {'semi': 'R16', 'addsub': 'R16', 'multdiv': 'R16', 'rparen': 'R16', 'comp': 'R16'},
    {'semi': 'R17', 'addsub': 'R17', 'multdiv': 'R17', 'rparen': 'R17', 'comp': 'R17'},
    {'rparen': 'S37'},
    {'id': 'S38', },  # 30
    {'rbrace': 'S39'},
    {'vtype': 'S6', ' rbrace': 'R37', 'VDECL': 32, 'FDECL': 33, 'ODECL': 40},
    {'vtype': 'S6', ' rbrace': 'R37', 'VDECL': 32, 'FDECL': 33, 'ODECL': 41},
    {'id': 'S27', 'lparen': 'S26', 'num': 'S28', 'EXPR': 42, 'TERM': 24, 'FACTOR': 25},
    {'id': 'S27', 'lparen': 'S26', 'num': 'S28', 'TERM': 43, 'FACTOR': 25},  # 35
    {'rparen': 'S44'},
    {'lbrace': 'S45'},
    {'rparen': 'R22', 'comma': 'S47', 'MOREARGS': 46},
    {'vtype': 'R34', 'class': 'R34', '$': 'R34'},
    {'rbrace': 'R35'},  # 40
    {'rbrace': 'R36'},
    {'semi': 'R11', 'rparen': 'R11'},
    {'semi': 'R13', 'addsub': 'R13', 'rparen': 'R13'},
    {'semi': 'R15', 'addsub': 'R15', 'multdiv': 'R15', 'rparen': 'R15', 'comp': 'R15'},
    {'vtype': 'S2', 'id': 'S54', 'rbrace': 'R24', 'if': 'S52', 'while': 'S53', 'return': 'R24', 'VDECL': 50, 'ASSIGN': 51, 'BLOCK': 48, 'STMT': 49},  # 45
    {'rparen': 'R19'},
    {'vtype': 'S55'},
    {'return': 'S57', 'RETURN': 56},
    {'vtype': 'S2', 'id': 'S54', 'rbrace': 'R24', 'if': 'S52', 'while': 'S53', 'return': 'R24', 'VDECL': 50, 'ASSIGN': 51, 'BLOCK': 58, 'STMT': 49},
    {'vtype': 'R25', 'id': 'R25', 'rbrace': 'R25', 'if': 'R25', 'while': 'R25', 'return': 'R25'},  # 50
    {'semi': 'S59'},
    {'lparen': 'S60'},
    {'lparen': 'S61'},
    {'assign': 'S15'},
    {'id': 'S62'},  # 55
    {'rbrace': 'S63'},
    {'id': 'S27', 'literal': 'S21', 'character': 'S22', 'boolstr': 'S23', 'lparen': 'S26', 'num': 'S28', 'RHS': 64, 'EXPR': 20, 'TERM': 24, 'FACTOR': 25},
    {'rbrace': 'R23', 'return': 'R23'},
    {'vtype': 'R26', 'id': 'R26', 'rbrace': 'R26', 'if': 'R26', 'while': 'R26', 'return': 'R26'},
    {'id': 'S27', 'boolstr': 'S67', 'lparen': 'S26', 'num': 'S28', 'FACTOR': 66, 'COND': 65},  # 60
    {'id': 'S27', 'boolstr': 'S67', 'lparen': 'S26', 'num': 'S28', 'FACTOR': 66, 'COND': 68},
    {'rparen': 'R22', 'comma': 'S47', 'MOREARGS': 69},
    {'vtype': 'R18', 'rbrace': 'R18', 'class': 'R18', '$': 'R18'},
    {'semi': 'S70'},
    {'rparen': 'S71'},  # 65
    {'comp': 'S72'},
    {'rparen': 'R30'},
    {'rparen': 'S73'},
    {'rparen': 'R21'},
    {'rbrace': 'R33'},  # 70
    {'lbrace': 'S74'},
    {'id': 'S27', 'lparen': 'S26', 'num': 'S28', 'FACTOR': 75},
    {'lbrace': 'S76'},
    {'vtype': 'S2', 'id': 'S54', 'rbrace': 'R24', 'if': 'S52', 'while': 'S53', 'return': 'R24', 'VDECL': 50, 'ASSIGN': 51, 'BLOCK': 77, 'STMT': 49},
    {'rparen': 'R29'},  # 75
    {'vtype': 'S2', 'id': 'S54', 'rbrace': 'R24', 'if': 'S52', 'while': 'S53', 'return': 'R24', 'VDECL': 50, 'ASSIGN': 51, 'BLOCK': 78, 'STMT': 49},
    {'rbrace': 'S79'},
    {'rbrace': 'S80'},
    {'vtype': 'R32', 'id': 'R32', 'rbrace': 'R32', 'if': 'R32', 'while': 'R32', 'else': 'S82', 'return': 'R32'},
    {'vtype': 'R28', 'id': 'R28', 'rbrace': 'R28', 'if': 'R28', 'while': 'R28', 'return': 'R28'},  # 80
    {'vtype': 'R27', 'id': 'R27', 'rbrace': 'R27', 'if': 'R27', 'while': 'R27', 'return': 'R28'},
    {'lbrace': 'S83'},
    {'vtype': 'S2', 'id': 'S54', 'rbrace': 'R24', 'if': 'S52', 'while': 'S53', 'return': 'R24', 'VDECL': 50, 'ASSIGN': 51, 'BLOCK': 84, 'STMT': 49},
    {'rbrace': 'S85'},
    {'vtype': 'R31', 'id': 'R31', 'rbrace': 'R31', 'if': 'R31', 'while': 'R31', 'return': 'R31'}
]


END_MARK = '$'
terminal_list = []

lines = f.readlines()
for line in lines:
    terminal = line.split()[0]
    terminal_list.append(terminal)


terminal_list.append(END_MARK)
error_checker = copy.deepcopy(terminal_list)
# print(terminal_list)


def main():

    if len(terminal_list) == 1:
        return True, ''

    SLR_stack = [0]
    splitter = 0
    error_line = 1

    while True:
        current_state = SLR_stack[-1]

        next_symbol = terminal_list[splitter]

        print("스플리터 : ", splitter)
        #print(next_symbol)
        #print(current_state)
        #print(SLR_TABLE[current_state])
        # 판단할 수 없는 terminal이 있으면 error
        if next_symbol not in SLR_TABLE[current_state].keys():
            error = "[Error] Error in line " + str(error_line) + ", " + error_checker[error_line-1]
            print(error)
            return False, error

        # shift
        #print(SLR_TABLE[current_state][next_symbol][0])
        if SLR_TABLE[current_state][next_symbol][0] == 'S':
            print("SHIFT")
            splitter += 1
            error_line += 1
            SLR_stack.append(int(SLR_TABLE[current_state][next_symbol][1:]))
            print(SLR_stack)

        # Reduce
        elif SLR_TABLE[current_state][next_symbol][0] == 'R':
            print("REDUCE")
            table_num = SLR_TABLE[current_state][next_symbol][1:]
            print("테이블 넘 ", table_num)
            #print(type(buf_string))
            rule = str(RULE[int(table_num)].values())
            lengh = len(rule.split(" "))  # 룰의 어절의 개수

            print("길이 : ", lengh)
            print("버프 룰 : ", rule)

            for i in range(lengh):
                print(rule)
                if rule != 'epsilon':
                    # print("스택에는 ", SLR_stack)
                    SLR_stack.pop()
                    terminal_list.pop(splitter-i-1)
                    print("스택에는 ", SLR_stack)
            if rule != 'epsilon':
                splitter = splitter - len(rule) + 1
            else:
                splitter += 1

            terminal_list.insert(splitter-1, rule[0])
            current_state = SLR_stack[-1]

            if (rule[0] == 'S') and (len(terminal_list) == 2) and (splitter == 1):
                return True, ''
            if rule[0] not in SLR_TABLE[current_state].keys():
                error = "[Error] Error in line " + str(error_line) + ", " + error_checker[error_line - 1]
                print(error)
                return False, error

            SLR_stack.append(SLR_TABLE[current_state][rule[0]])


        #return True

main()
