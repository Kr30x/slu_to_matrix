import pyperclip

n, var_num = list(map(int, input("Количество уравнений в СЛУ и количество переменных (здесь, количество столбцов в матрице): ").split()))
ans = ''
eqs = []
for i in range(1, n + 1):
    eq = list(map(int, input().split()))
    eqs.append(eq)
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
            ans += "{" + f"{matrix[i][j]}" + '}'
        ans += r"{|}"
        ans += "{" + f"{matrix[i][-1]}" + '}'
        ans += '}'
    return ans


def print_matrix():
    global eqs
    for i, line in enumerate(eqs):
        print(f"{i + 1}:", *line)


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
        to, line, koef = list(map(float, input("to, line, koef: ").split()))
        to = int(to)
        line = int(line)
        add_to_line_lambda(to, line, koef)
    if cmd == "swap":
        a, b = list(map(int, input("line1, line2: ").split()))
        swap(a, b)
    if cmd == "mult":
        line, koef = list(map(float, input("line, koef: ").split()))
        line = int(line)
        mult(line, koef)
    if cmd == "del":
        line = int(input("line: "))
        delete(line)
    if cmd == "set":
        line = int(input("line: "))
        eqs = list(map(int, input(f"{line}: ").split()))
    if cmd == "end":
        exit(0)
