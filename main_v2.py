import sys
import pyperclip
import os
import signal
import argparse

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    clear_screen()
    print("\nCtrl+C pressed. Exiting the program. Goodbye!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Matrix Operations Script")
parser.add_argument("-raw", action="store_true", help="Enable raw mode (no divider in LaTeX and console output)")
parser.add_argument("-dn", action="store_true", help="Use default LaTeX notation (\\begin{pmatrix} and \\end{pmatrix})")
args = parser.parse_args()

def help_function():
    print("""
Available commands:
  help                 - Show this help message
  add <to> <from> <k>  - Add k times row <from> to row <to>
  swap <a> <b>         - Swap rows a and b
  mult <line> <k>      - Multiply row <line> by k
  del <line>           - Delete row <line>
  set <line> <values>  - Set row <line> to the given values
  end                  - Exit the program

You can also press Ctrl+C at any time to exit the program.
    """)

clear_screen()
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
if not args.raw:
    var_num += 1

def get_string(matrix):
    global n
    global var_num
    ans = ""
    
    if args.dn or n > 5:
        ans += r"\begin{pmatrix}"
    elif n == 2:
        ans += r"\mattwo"
    elif n == 3:
        ans += r"\matthree"
    elif n == 4:
        ans += r"\matfour"
    elif n == 5:
        ans += r"\matfive"
    
    for i in range(n):
        if args.dn:
            row_content = []
            for j in range(var_num):
                if j < var_num - 1:
                    if eqs[i][j] < 0 or consts[i][j] == "":
                        row_content.append(f"{consts[i][j]}{matrix[i][j]}")
                    else:
                        if eqs[i][j] != 0:
                            row_content.append(f"{consts[i][j]}+{matrix[i][j]}")
                        else:
                            row_content.append(f"{consts[i][j]}")
                else:
                    row_content.append(f"{matrix[i][j]}")
            
            ans += " & ".join(row_content)
        else:
            if var_num == 3:
                ans += r"\rowthree"
            elif var_num == 4:
                ans += r"\rowfour"
            elif var_num == 5:
                ans += r"\rowfive"
            elif var_num == 6:
                ans += r"\rowsix"
            elif var_num == 7:
                ans += r"\rowseven"
            elif var_num == 8:
                ans += r"\roweight"
            elif var_num == 9:
                ans += r"\rownine"
            else:
                ans += "&".join(["{}" for _ in range(var_num)])
            
            for j in range(var_num - 1):
                if eqs[i][j] < 0 or consts[i][j] == "":
                    ans += "{" + f"{consts[i][j]}{matrix[i][j]}" + '}'
                else:
                    if eqs[i][j] != 0:
                        ans += "{" + f"{consts[i][j]}+{matrix[i][j]}" + '}'
                    else:
                        ans += "{" + f"{consts[i][j]}" + '}'
            if not args.raw:
                ans += r"{|}"
            ans += "{" + f"{matrix[i][-1]}" + '}'
        
        if i < n - 1:
            ans += r" \\"
    
    if args.dn or n > 5:
        ans += r"\end{pmatrix}"
    
    return ans

def print_matrix():
    global eqs, consts
    max_width = max(max(len(f"{consts[i][j]}{eqs[i][j]}") for j in range(len(eqs[i]))) for i in range(len(eqs)))
    
    for i, line in enumerate(eqs):
        print(f"{i + 1}:", end="\t")
        for j in range(len(line)):
            if eqs[i][j] < 0 or consts[i][j] == "":
                value = f"{consts[i][j]}{eqs[i][j]}"
            else:
                if eqs[i][j] != 0:
                    value = f"{consts[i][j]}+{eqs[i][j]}"
                else:
                    value = f"{consts[i][j]}"
            print(f"{value:>{max_width}}", end="\t")
            if j == len(line) - 2 and not args.raw:
                print("|", end="\t")
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

def display_current_state():
    clear_screen()
    print("Current matrix state:")
    print_matrix()
    print("\nLaTeX representation:")
    print(get_string(eqs))
    print("\nType 'help' for a list of available commands.")
    print("Press Ctrl+C to exit the program.")

display_current_state()

while True:
    try:
        cmd_input = input("\nEnter command and arguments: ").split()
        cmd = cmd_input[0] if cmd_input else ""
        
        try:
            if cmd == "help":
                clear_screen()
                help_function()
                input("\nPress Enter to continue...")
            elif cmd == "add":
                to, line, koef = map(float, cmd_input[1:4])
                add_to_line_lambda(int(to), int(line), koef)
            elif cmd == "swap":
                a, b = map(int, cmd_input[1:3])
                swap(a, b)
            elif cmd == "mult":
                line, koef = float(cmd_input[1]), float(cmd_input[2])
                mult(int(line), koef)
            elif cmd == "del":
                line = int(cmd_input[1])
                delete(line)
            elif cmd == "set":
                line = int(cmd_input[1])
                eqs[line-1] = list(map(int, cmd_input[2:]))
            elif cmd == "end":
                clear_screen()
                print("Exiting the program. Goodbye!")
                exit(0)
            else:
                raise ValueError('Unknown command')
        except (ValueError, IndexError) as e:
            clear_screen()
            print(f'Error: {str(e)}. Type "help" for correct command usage.', file=sys.stderr)
            input("\nPress Enter to continue...")
        
        if cmd != "help":
            pyperclip.copy(get_string(eqs))
            display_current_state()
    except KeyboardInterrupt:
        clear_screen()
        print("\nCtrl+C pressed. Exiting the program. Goodbye!")
        sys.exit(0)
