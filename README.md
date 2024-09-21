# slu_to_matrix
Упрощает работу с расширенными матрицами для решения СЛУ

# Установка
1) скачать файлы ```main_v2.py``` и ```gset.sty``` (```main.py``` старая версия) 
2) В терминале установить с помощью команды ```pip install pyperclip``` библиотеку для операций с буфером обмена

# Флаги

```-raw``` - Для работы с обычными матрицами, не добавляется разделитель 

```-dn``` - По дефолту используется gset notation, этот флаг меняет на ```\begin{pmatrix}``` notation

# gset представление матриц
Mat(m, n) = \matrix_m{\row_n{elem1, elem2, ..., elem_n}}{...} \
Mat(m, n) = \matrix_m{elem1_1 & elem1_2, ... & elem1_n}{...}\
Это представление сделано для LaTeX и работает с пакетом gset.sty \
Сейчас поддерживаются матрицы с размером до m = 5, n = 9. 
Убедитесь, что пакет gset.sty установлен в папку вместе с вашим LaTeX проектом.
Чтобы подключить пакет в LaTeX используйте команду ```\usepackage{gset}```.

# Как использовать
1) Задать количество строк и столбцов в матрице
2) Задать матрицу построчно, разделяя элементы пробелом
3) Использовать команды для преобразования матрицы
4) После каждой команды в буфер обмена будет скопирован gset код полученной матрицы, матрица изменится в самой программе
5) Использовать полученный gset код в LaTeX документе

# Команды
1) ```add (insert_line, addition_line, koef)``` -> добавляет ```addition_line``` к ```insert_line``` с коэффициентом ```koef```
2) ```swap (line1, line2)``` -> меняет местами ```line1``` и ```line2```
3) ```mult (line, koef)``` -> умножает ```line``` на коэффициент ```koef```
4) ```del (line)``` -> удаляет ```line```
5) ```set (line)``` -> заменяет ```line``` новой введенной строкой
6) ```end ()``` -> завершает программу
6) ```help``` -> показывает эту подсказку
