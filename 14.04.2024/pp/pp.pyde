x=500
y=500
z=500
q=500
def setup():
    size(1000,1000)
def draw():
    background(255)
    global x, y, q ,z
    push()
    translate(x,x)
    ellipse(0,0,600,400)
    pop()
    
    push()
    translate(x,z)
    ellipse(0,0,600,400)
    pop()
    
    push()
    translate(z,q)
    ellipse(0,0,600,400)
    pop()
    
    push()
    translate(z,z)
    ellipse(0,0,600,400)
    pop()
    x = x - 10
    y = y + 10
    q = q - 10
    z = z + 10
    
  
    
