int npoints = 3; // number of points in the star
float radius1 = 100; // outer radius of the star
float radius2 = 50; // inner radius of the star

void setup() {
  size(800, 600);
}

void draw() {
  background(0); // set the background color to black

  // calculate the center of the screen
  float centerX = width / 2;
  float centerY = height / 2;

  // draw the star polygon at the center of the screen
  star(centerX, centerY, radius1, radius2, npoints);
}

// function to draw a star polygon
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

// function to handle mouse events
void mouseReleased() {
  // update the number of points in the star when the mouse is released
  npoints = npoints + 1;
  if (npoints > 10) {
    npoints = 3; // reset to 3 if the number of points is greater than 10
  }
}
