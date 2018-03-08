import math

def make_translate( x, y, z ):
    m = new_matrix()
    ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m

def make_scale( x, y, z ):
    m = new_matrix()
    ident(m)
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    return m

def make_rotX( theta ):
    theta = math.radians(theta)
    m = new_matrix()
    ident(m)
    m[1][1] = math.cos(theta)
    m[2][1] = math.sin(theta) * -1
    m[1][2] = m[2][1] * -1
    m[2][2] = m[1][1]
    return m
    
def make_rotY( theta ):
    theta = math.radians(theta)
    m = new_matrix()
    ident(m)
    m[0][0] = math.cos(theta)
    m[0][2] = -1 * math.sin(theta)
    m[2][0] = m[0][2] * -1
    m[2][2] = m[0][0]
    return m

def make_rotZ( theta ):
    theta = math.radians(theta)
    m = new_matrix()
    ident(m)
    m[0][0] = math.cos(theta)
    m[1][0] = math.sin(theta) * -1
    m[0][1] = m[1][0] * -1
    m[1][1] = m[0][0]
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix ) ):
        for c in range( len(matrix[r]) ):
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
'''def matrix_mult( m1, m2 ):
    ans = new_matrix(len(m1),len(m2[0]))
    for cellr in range(len(ans)):
        for cellc in range(len(ans[0])):
            for c in range(len(ans)):
               ans[cellr][cellc] += m1[cellr][c] * m2[c][cellc]
    m2[:] = list(ans)
    print_matrix(m1)
    print_matrix(m2)'''

'''def getCol(m, c):
    col = []
    for r in range(len(m)):
        col.append(m[r][c])
    return col
    
def matrix_mult( m1, m2 ):
    print_matrix(m1)
    print_matrix(m2)
    ans = new_matrix2(len(m1),len(m2[0]))
    for r in range(len(ans)):
        for c in range(len(ans[0])):
            for x in range(len(ans)):
                ans[r][c] += m1[r][x] * m2[x][c]
    m2[:] = ans'''

def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

'''def new_matrix2(rows, cols):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m'''
