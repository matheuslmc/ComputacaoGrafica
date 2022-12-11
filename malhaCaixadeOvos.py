from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from random import random
import math

cores = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
    (1, 0, 1),
    (0.5, 1, 1),
    (1, 0, 0.5),
)


def fxy(x, y):
    return (math.sin(x) * math.cos(y)) / 6


def malha(h, n, r):
    #essa parte recebi auxilio de Nycolas Vycas para o tratamento da funcao.
    vertices = []
    faces = []
    colors = []

    r = 20
    for i in range(r):
        for j in range(r):
            vertices.append([i / r - 0.5, fxy(j + r / 2, i + r),j / r - 0.5,])

    for indice in range(len(vertices)):
        if indice % r == 0:
            continue
        if indice / r > r - 1:
            continue
        indice = indice - 1
        bottom_face = [indice, indice + r, indice + 1]
        top_face = [indice + 1, indice + r + 1, indice + r]
        faces.append(bottom_face)
        faces.append(top_face)

    for face in faces:
        color = (
            face[0] / len(vertices),
            face[1] / len(vertices),
            face[2] / len(vertices),
        )
        color = list(color)
        colors.append(color)

    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 0, 1, 0)
    glRotatef(2, 1, 0, 0)
    malha(2, 6, 3)
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Caixa de Ovos")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -2)
glutTimerFunc(10, timer, 1)
glutMainLoop()
