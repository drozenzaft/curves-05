import math

def make_bezier():
    m = new_matrix()
    m[0][0] = -1
    m[0][1] = 3
    m[0][2] = -3
    m[0][3] = 1
    m[1][0] = 3
    m[1][1] = -6
    m[1][2] = 3
    m[2][0] = -3
    m[2][1] = 3
    m[3][0] = 1
    return m

def make_hermite():
    m = new_matrix()
    m[0][0] = 2
    m[1][0] = -2
    m[2][0] = 1
    m[3][0] = 1
    m[0][1] = -3
    m[1][1] = 3
    m[2][1] = -2
    m[3][1] = -1
    m[2][2] = 1
    m[0][3] = 1
    return m

def generate_curve_coefs( p0, p1, p2, p3, t ):
    m = new_matrix()
    if t == 'hermite':
        m = make_hermite()
    elif t == 'bezier':
        m = make_bezier()
    ptm = new_matrix2(1,4)
    ptm[0][0] = p0
    ptm[0][1] = p1
    ptm[0][2] = p2
    ptm[0][3] = p3
    matrix_mult(m,ptm)
    return ptm

def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    return t

def make_scale( x, y, z ):
    t = new_matrix()
    ident(t)
    t[0][0] = x
    t[1][1] = y
    t[2][2] = z
    return t

def make_rotX( theta ):
    t = new_matrix()
    ident(t)
    t[1][1] = math.cos(theta)
    t[2][1] = -1 * math.sin(theta)
    t[1][2] = math.sin(theta)
    t[2][2] = math.cos(theta)
    return t

def make_rotY( theta ):
    t = new_matrix()
    ident(t)
    t[0][0] = math.cos(theta)
    t[0][2] = -1 * math.sin(theta)
    t[2][0] = math.sin(theta)
    t[2][2] = math.cos(theta)
    return t

def make_rotZ( theta ):
    t = new_matrix()
    ident(t)
    t[0][0] = math.cos(theta)
    t[1][0] = -1 * math.sin(theta)
    t[0][1] = math.sin(theta)
    t[1][1] = math.cos(theta)
    return t

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(len(m2[0])):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1

def new_matrix(rows=4,cols=4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

def new_matrix2(rows,cols):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
