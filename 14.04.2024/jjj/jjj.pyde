x=10
def setup():
    size(1000,1000)
def draw():
    push()
    global x
    translate(x,0)
    triangle(0,0,200,00,100,100)
    translate(0,x)
    triangle(0,0,200,00,100,100)
    translate(0,x)
    triangle(0,0,200,00,100,100)
    pop()
    x = x + 10
