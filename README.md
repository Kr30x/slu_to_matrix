# slu_to_matrix
Simplifies transformation of extended matrices with integer elements

#installation
1) download files from repository
2) use ```pip install pyperclip``` to download required library for clipboard operations
3) That's it!


# gset matrix view
Mat(m, n) = \matrix_m{\row_n{elem1, elem2, ..., elem_n}}{...} \
This view is made for LaTeX and works with file gset.sty \
Right now there are matrices up to m = 4, n = 5. 
Be sure to istall it with your LaTeX project.
To use package write ```\usepackage{gset}``` command in your LaTeX editor.

# how to use
1) Set number of variables and equasions
2) use commands to operate with matrix
3) input arguments for command
4) after each command a matrix code in gset structure will be copied to your clipboard

# commands 
1) ```add (insert_line, addition_line, koef)``` -> ads addition_line to insert_line with coefficient koef
2) ```swap (line1, line2)``` -> swaps line1 and line2
3) ```mult (line, koef)``` -> multiplies line by coefficient koef
4) ```del (line)``` -> deletes line
5) ```set (line)``` -> replaces line with new inputed line
6) ```end ()``` -> ends the program
