import sys

import pyperclip

n, var_num = list(map(int, input(
    "Количество уравнений в СЛУ и количество переменных (здесь, количество столбцов в матрице): ").split()))
ans = ''
eqs = [0] * n
consts = [0] * n
for i in range(n):
    line = input().split()
    eqs[i] = [0] * len(line)
    consts[i] = [""] * len(line)
    for j, item in enumerate(line):
        try:
            eqs[i][j] = int(item)
        except:
            consts[i][j] = item
var_num += 1


def get_string(matrix):
    global n
    global var_num
    ans = ""
    if n == 2:
        ans += "\mattwo"
    if n == 3:
        ans += "\matthree"
    if n == 4:
        ans += "\mtrfor"
    for i in range(n):
        ans += "{"
        if var_num == 3:
            ans += r"\rowthree"
        elif var_num == 4:
            ans += r"\rowfour"
        elif var_num == 5:
            ans += r"\rowfive"
        elif var_num == 6:
            ans += r"\rowsix"
        for j in range(var_num - 2):
            if eqs[i][j] < 0:
                ans += "{" + f"{consts[i][j]}{matrix[i][j]}" + '}'
            else:
                if eqs[i][j] != 0:
                    ans += "{" + f"{consts[i][j]}+{matrix[i][j]}" + '}'
                else:
                    ans += "{" + f"{consts[i][j]}" + '}'
        ans += r"{|}"
        ans += "{" + f"{matrix[i][-1]}" + '}'
        ans += '}'
    return ans


def print_matrix():
    global eqs
    for i, line in enumerate(eqs):
        print(f"{i + 1}:", end="")
        for j in range(len(line)):
            if eqs[i][j] < 0 or consts[i][j] == "":
                print(f"{consts[i][j]}{eqs[i][j]}", end=" ")
            else:
                if eqs[i][j] != 0:
                    print(f"{consts[i][j]}+{eqs[i][j]}", end=" ")
                else:
                    print(f"{consts[i][j]}", end=" ")
        print()


def add_to_line_lambda(to, line, l):
    global eqs
    for i in range(len(eqs[to - 1])):
        eqs[to - 1][i] += eqs[line - 1][i] * l
        if eqs[to - 1][i] == int(eqs[to - 1][i]):
            eqs[to - 1][i] = int(eqs[to - 1][i])


def swap(a, b):
    global eqs
    eqs[a - 1], eqs[b - 1] = eqs[b - 1], eqs[a - 1]


def mult(line, koef):
    global eqs
    for i in range(len(eqs[line - 1])):
        eqs[line - 1][i] *= koef
        if eqs[line - 1][i] == int(eqs[line - 1][i]):
            eqs[line - 1][i] = int(eqs[line - 1][i])


def delete(line):
    global eqs
    global n
    n -= 1
    eqs.pop(line - 1)


while True:
    print_matrix()
    print(get_string(eqs))
    pyperclip.copy(get_string(eqs))
    cmd = input("cmd: ")
    if cmd == "add":
        try:
            to, line, koef = list(map(float, input("to, line, koef: ").split()))
            to = int(to)
            line = int(line)
            add_to_line_lambda(to, line, koef)
        except:
            print('bad input', file=sys.stderr)
    if cmd == "swap":
        try:
            a, b = list(map(int, input("line1, line2: ").split()))
            swap(a, b)
        except:
            print('bad input', file=sys.stderr)
    if cmd == "mult":
        try:
            line, koef = list(map(float, input("line, koef: ").split()))
            line = int(line)
            mult(line, koef)
        except:
            print('bad input', file=sys.stderr)
    if cmd == "del":
        try:
            line = int(input("line: "))
            delete(line)
        except:
            print('bad input', file=sys.stderr)
    if cmd == "set":
        try:
            line = int(input("line: "))
            eqs = list(map(int, input(f"{line}: ").split()))
        except:
            print('bad input', file=sys.stderr)
    if cmd == "end":
        exit(0)
