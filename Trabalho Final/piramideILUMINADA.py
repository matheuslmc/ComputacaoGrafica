from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GL import glLightfv, GL_LIGHT0, GL_POSITION, GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR
import sys 
N = 4
 
vertices = (
    ( 2, 0, 2),
    ( 2, 0,-2),
    (-2, 0,-2),
    (-2, 0, 2),
    ( 0, 2, 0),
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
 
cores = ( (1,0.5,2),(1,1,0),(2,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
 
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
    mat_ambient = (0.5, 0.5, 0.5, 1.0)
    mat_diffuse = (1.0, 1.0, 1.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (50.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)
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

    light_ambient = (0.5, 0.5, 0.5, 1.0)
    light_diffuse = (1.0, 1.0, 1.0, 1.0)
    light_specular = (1.0, 1.0, 1.0, 1.0)
    light_position = (5.0, 5.0, 5.0, 0.0)
    #glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    #glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)


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
glutInitWindowSize(600,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,0.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()