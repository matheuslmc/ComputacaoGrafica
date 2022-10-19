function setup() {
  
    // Create canvas size 
    createCanvas(150, 110);
}
   
function draw() {
  
    // Set the background color
    background(220);
      
    noFill();
      
    // Set the stroke color
    stroke(0, 0, 0);
      
    // Bezier function 8 parameters 
    // except z-coordinate
    bezier(85, 20, 10, 10, 160, 90, 50, 80);
}
