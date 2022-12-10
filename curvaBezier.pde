//Definindo os 4 pontos da curva.
PVector p0, p1, p2, p3;

void setup() {
  //Tamanho da tela
  size(500, 500);

  // COlocando os pontos iniciais
  p0 = new PVector(100, 100);
  p1 = new PVector(200, 100);
  p2 = new PVector(300, 300);
  p3 = new PVector(400, 100);
}

void draw() {
  // Limpando a tela...
  background(255);

  // Desenhando a cruva
  noFill();
  stroke(0);
  bezier(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);

  // Desenhando os pontos de controle
  fill(0);
  noStroke();
  ellipse(p0.x, p0.y, 10, 10);
  ellipse(p1.x, p1.y, 10, 10);
  ellipse(p2.x, p2.y, 10, 10);
  ellipse(p3.x, p3.y, 10, 10);
}

// Função para mexer os pontos usando Mouse.
void mouseDragged() {
  // Se o mouse estiver sobre um ponto de controle, mova-o para a posição atual do mouse
  if (dist(mouseX, mouseY, p0.x, p0.y) < 10) {
    p0.x = mouseX;
    p0.y = mouseY;
  }
  else if (dist(mouseX, mouseY, p1.x, p1.y) < 10) {
    p1.x = mouseX;
    p1.y = mouseY;
  }
  else if (dist(mouseX, mouseY, p2.x, p2.y) < 10) {
    p2.x = mouseX;
    p2.y = mouseY;
  }
  else if (dist(mouseX, mouseY, p3.x, p3.y) < 10) {
    p3.x = mouseX;
    p3.y = mouseY;
  }
}
