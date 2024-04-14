x=100
g=0
def setup():
    size(1000,1000)
def draw():
    global x,g
    push()
    rectMode(CENTER)
    fill(g)
    rect(500,500,x,x)
    pop()
    x=x+1
    g=g+1
    if x>=350:
        noLoop()
