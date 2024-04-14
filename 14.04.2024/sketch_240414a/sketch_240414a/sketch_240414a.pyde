d=0
x=1000
w=0
q=1000
def setup():
    size(1000,1000)
def draw():
    fill(d,0,0)
    ellipse(1000,x,100,100)
    fill(d,255,33)
    ellipse(w,w,100,100)
    fill(d,78,255)                                   
    ellipse(20,q,100,100)
    global  x,w,q,d
    x=x-10
    w=w+10
    q=q-10
    d=d+1
