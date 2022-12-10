int npoints = 3; // pontos da estrela
float radius1 = 100; // raio de fora 
float radius2 = 50; // raio de dentro

void setup() {
  size(800, 600);
}

void draw() {
  background(0); // cor preta de fundo

  // calcula o meio da tela
  float centerX = width / 2;
  float centerY = height / 2;

  // desenha o poligono estrelado no meio da tela
  star(centerX, centerY, radius1, radius2, npoints);
}

// Função para desenhar o poligono estrelado.
void star(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle / 2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a + halfAngle) * radius1;
    sy = y + sin(a + halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}

// Função para o Mouse
void mouseReleased() {
  // A cada clique, soma +1 vertice de fora.
  npoints = npoints + 1;
  if (npoints > 10) {
    npoints = 3; // Valor se torna 3 caso chegue a 10.
}
