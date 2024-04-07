x=20
y=1000
def setup():
    size(600,600)
def draw():
    global x , y
    fill(random(0,255))
    ellipse(x,0,125,100)
    ellipse(y,100,125,100)
    ellipse(x,200,125,100)
    ellipse(y,300,125,100)
    ellipse(x,400,125,100)
    ellipse(y,500,125,100)
    ellipse(x,600,125,100)
    x=x+10 
    y=y-10
