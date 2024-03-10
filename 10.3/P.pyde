x=0
y=0
def setup():
    size(1000,1000)
def draw():
    noFill()
    global x,y
    translate(x,y)
    triangle(437,125,62, 875, 875, 875)
    triangle(437,562,375,624,500,624)
    triangle(250,813,187,937,312,937)
    triangle(437,813,375,937,500,937)
    triangle(624,813,562,937,680,937)
    x = x + 4
    y = y + 4
