x=10
def setup():
    fill(252,255,255)
    size(1400,1400)
    
def draw():
    global x
    background(255)
    x=x+1
    translate(x,0)
    fill(255,224,224)
    rect(50,20,40,30)
    fill(240)
    rect(40,50,60,40)
    fill(240,0,0)
    rect(20,50,20,60)
    fill(0)
    rect(100,50,20,60)
    fill(231,240,0)
    rect(40,90,30,50)
    fill(0,225,240)
    rect(70,90,30,50)
    line(60,40,80,40)
    strokeWeight(5)
    point(60,30)
    point(80,30)
