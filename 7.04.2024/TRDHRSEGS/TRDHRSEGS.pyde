q=500
w=300
e=400
x=200
def setup():
    size(1000,1000)
def draw():
    global x,w,e,q
    rectMode(CENTER)
    rect(q,x,e,w)
    # x=x+5
    w=w+5
    e=e+5
    # q=q+5
    
