from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math
   
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5))
 
def prismas(h,n,r):
    
    vertices = []
    a = 2*math.pi/n
    for i in range(0,n):
        x = r*math.cos(i*a)
        y = 0
        z = r*math.sin(i*a)
        vertices += [[x,y,z]] #prencheu a base de baixo
    for i in range(0,n):
        x = r*math.cos(i*a)
        y = h
        z = r*math.sin(i*a)
        vertices += [[x,y,z]] #prencheu a base de cima

    print(vertices)
    
    faces = []
    for i in range(0,n):
        if(i==n-1):
            faces += [[i,0,n,2*n-1]]
        else:
            faces += [[i,i+1,n+i+1,n+i]]

    k=0
    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv(cores[k%len(cores)])
        k += 1
        for v in face:
            glVertex3fv(vertices[v])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3fv(cores[1])
    for v in range(0,n):
        glVertex3fv(vertices[v])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3fv(cores[4])
    for x in range(n,2*n):
        glVertex3fv(vertices[x])
    glEnd()
    
       
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glTranslatef(0,0,0)
    glRotatef(2,1,0,0);
    prismas(2,6,3)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
