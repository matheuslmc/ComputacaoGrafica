from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos,sin,pi


r=1
details = 140
p=[]

for i in range(0,details+1):
    theta = (i * pi / details)-(pi/2)
    for j in range(0,details+1):
        phi = (j * 2 * pi / details)
        p+=[[r*cos(theta)*cos(phi),r*sin(theta),r*cos(theta)*sin(phi)]]
    

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def PEsfera():

    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    for ponto in p:
        glVertex3fv(ponto)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,0.9)
    for ponto in p:
        glVertex3fv(ponto)
    glEnd()

def Esfera():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,0)
    PEsfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(20,timer,1)

# PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(Esfera)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-6)
glRotatef(0,1,1,1)
glutTimerFunc(8,timer,1)
glutMainLoop()
