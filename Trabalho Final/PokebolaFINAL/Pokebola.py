from array import array
from OpenGL import GL
import ctypes

scale = 10

class Pokebola:

    def __init__(self):
        scale = 1
        state = 0
        vertexCount = 0
        faceCount = 0
        vertices = array("f")
        indices = array("I")
        with open("objs/pokebola.ply", "r") as f:
            for line in f:
                parts = line.split()
                if state == 0: # HEADER
                    if len(parts)>0 and parts[0] == "end_header":
                        state = 1
                    else:
                        if len(parts) == 3 and parts[0] == "element":
                            if parts[1] == "vertex":
                                vertexCount = int(parts[2])
                            elif parts[1] == "face":
                                faceCount = int(parts[2])
                elif state == 1: # VERTEX
                    vertices.append(float(parts[0])*scale)
                    vertices.append(float(parts[1])*scale)
                    vertices.append(float(parts[2])*scale)
                    vertices.append(float(parts[3]))
                    vertices.append(float(parts[4]))
                    vertices.append(float(parts[5]))
                    vertexCount -= 1
                    if vertexCount == 0:
                        state = 2
                else: # STATE == 2 -> FACES
                    faceVertexCount = int(parts[0])
                    for i in range(2,faceVertexCount):
                        indices.append(int(parts[1]))
                        indices.append(int(parts[i]))
                        indices.append(int(parts[i+1]))
                    faceCount-=1
                    if faceCount == 0:
                        break

        self.arrayBufferId = GL.glGenVertexArrays(1)
        self.N = len(indices)
        GL.glBindVertexArray(self.arrayBufferId)
        GL.glEnableVertexAttribArray(0) # POSITION
        GL.glEnableVertexAttribArray(1) # Normal

        idBuffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idBuffer)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, len(vertices)*vertices.itemsize, ctypes.c_void_p(vertices.buffer_info()[0]), GL.GL_STATIC_DRAW)
        stride = 6*ctypes.sizeof(ctypes.c_float)
        normalPointer = ctypes.c_void_p(6*ctypes.sizeof(ctypes.c_float))
        GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,stride,ctypes.c_void_p(0))
        GL.glVertexAttribPointer(1,3,GL.GL_FLOAT,GL.GL_FALSE,stride,normalPointer)

        idIndex = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, idIndex)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(indices)*indices.itemsize, ctypes.c_void_p(indices.buffer_info()[0]), GL.GL_STATIC_DRAW)

    def draw(self):
        GL.glBindVertexArray(self.arrayBufferId)
        GL.glDrawElements(GL.GL_TRIANGLES, self.N, GL.GL_UNSIGNED_INT, ctypes.c_void_p(0))
