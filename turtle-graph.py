import turtle as t

t.bgcolor("black")
t.color("yellow")
t.speed(10) # maximum speed

angle = 10

for i in range(10):
    angle = angle + 5
    for px in range(150):
        t.forward(px)
        t.left(angle)
    t.clear()
