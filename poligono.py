from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

N = 8
 
vertices = (
    ( 1, 0, 1),
    ( 1, 0,-1),
    (-1, 0,-1),
    (-1, 0, 1),
    ( 0, 7, 0),
    )
 
linhas = (
    (0,1),
    (0,3),
    (0,4),
    (1,2),
    (1,4),
    (2,3),
    (2,4),
    (3,4),
    )
 
faces = (
    (0,1,2),
    (0,2,3),
    (0,1,4),
    (1,2,4),
    (2,3,4),
    (0,3,4),
    )
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
 
def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()
 
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()
 
a = 0
 

     
 
 
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(-a,0,2,0)
    Piramide()
    glPopMatrix()
    
    glutSwapBuffers()
    a += 1
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
