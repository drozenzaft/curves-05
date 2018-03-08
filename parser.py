from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguments (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
#rounding the final matrix
def roundMatrix(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            m[r][c] = int(m[r][c])
          
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    f = f.read()
    g = f.split('\n')
    for c in range(len(g)):
        g[c] = g[c].split(' ')
        for k in range(len(g[c])):
            if g[c][k].isdigit():
                g[c][k] = int(g[c][k])
    i = 0
    while i < len(g):
        if g[i][0] == 'line':
            i += 1
            add_edge(points,g[i][0],g[i][1],g[i][2],g[i][3],g[i][4],g[i][5])
        elif g[i][0] == 'ident':
            ident(transform)
        elif g[i][0] == 'scale':
            i += 1
            s = make_scale(g[i][0],g[i][1],g[i][2])
            matrix_mult(s,transform)
        elif g[i][0] == 'move':
            i += 1
            s = make_translate(g[i][0],g[i][1],g[i][2])
            matrix_mult(s,transform)
        elif g[i][0] == 'rotate':
            i += 1
            if g[i][0] == 'z':
                s = make_rotZ(g[i][1])
            elif g[i][0] == 'y':
                s = make_rotY(g[i][1])
            elif g[i][0] == 'x':
                s = make_rotX(g[i][1])
            matrix_mult(s,transform)
        elif g[i][0] == 'apply':
            matrix_mult(transform,points)
        elif g[i][0] == 'display':
            clear_screen(screen)
            roundMatrix(points)
            draw_lines(points,screen,color)
            display(screen)
        elif g[i][0] == 'save':
            roundMatrix(points)
            draw_lines(points,screen,color)
            i += 1
            save_extension(screen,g[i][0])
        i += 1
