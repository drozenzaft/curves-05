from display import *
from matrix import *

'''circle: adds a circle to the edge matrix - takes 4 parameters (cx, cy, cz, r)

hermite: adds a hermite curve to the edge matrix - takes 8 parameters (x0, y0, x1, y1, rx0, ry0, rx1, ry1)

The curve is between points (x0, y0) and (x1, y1).
(rx0, ry0) and (rx1, ry1) are the rates of change at each endpoint

bezier: adds a bezier curve to the edge matrix - takes 8 parameters (x0, y0, x1, y1, x2, y2, x3, y3)

This curve is drawn between (x0, y0) and (x3, y3)
(x1, y1) and (x2, y2) are the control points for the curve.'''

def add_circle( points, cx, cy, cz, r, step ):
    last_point_x = r + cx
    last_point_y = cy
    last_point_z = 0
    t = 0
    step *= 100
    while t <= 100:
        x = r * math.cos(2*math.pi*(t/100.0)) + cx
        y = r * math.sin(2*math.pi*(t/100.0)) + cy
        z = last_point_z
        add_edge(points,last_point_x,last_point_y,last_point_z,x,y,z)
        last_point_x = x
        last_point_y = y
        last_point_z = z
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    last_point_x = x0
    last_point_y = y0
    last_point_z = 0
    t = 0
    x = 0
    y = 0
    ptmx = new_matrix()
    ptmy = new_matrix()
    step *= 100
    while t <= 100:
        ptmx = generate_curve_coefs(x0,x1,x2,x3,curve_type)
        ptmy = generate_curve_coefs(y0,y1,y2,y3,curve_type)
        z = last_point_z
        x = ptmx[0][0]*((t/100.0) ** 3)+ ptmx[0][1]*((t/100.0) ** 2) + ptmx[0][2]*(t/100.0) + ptmx[0][3]
        y = ptmy[0][0]*((t/100.0) ** 3)+ ptmy[0][1]*((t/100.0) ** 2) + ptmy[0][2]*(t/100.0) + ptmy[0][3]
        add_edge(points,last_point_x,last_point_y,last_point_z,x,y,z)
        last_point_x = x
        last_point_y = y
        last_point_z = z
        t += step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
