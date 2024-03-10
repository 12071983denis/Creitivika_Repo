x=500
y=500
def setup():
    size(1000,1000)
def draw():
    noFill()
    global x,y
    ellipse(x,y,500,600)
    x = x - 4
    y = y + 4
