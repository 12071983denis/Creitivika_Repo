x=10
def setup():
    size(1000,1000)

def draw():
    background(255)
    global x
    ellipse(x,x,300,400)
    if x==1000:
        x=10
    x=x+5
    
    
