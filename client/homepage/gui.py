import turtle as t


def lturn():
    for i in range(18):
        t.lt(10)
        t.fd(1)


def rturn():
    for i in range(18):
        t.rt(10)
        t.fd(1)


t.home()
t.pencolor("white")
t.hideturtle()
t.begin_fill()
t.pensize(1)
t.speed(100)
t.lt(90)
t.fd(100)
lturn()
t.fd(100)
t.rt(90)
t.fd(100)
lturn()
t.fd(100)

t.rt(120)
t.fd(200)
lturn()
t.fd(180.1)
t.rt(150)

t.fd(300)
lturn()
t.fd(311)

t.rt(120)
t.fd(100)
lturn()
t.fd(100)
t.rt(150)
t.fd(100)

for i in range(9):
    t.lt(10)
    t.fd(1)
for i in range(9):
    t.fd(1)
    t.rt(10)
t.fd(90)
t.lt(90)
t.fd(100)
rturn()
t.fd(100)
t.lt(90)
t.fd(90)
rturn()
t.fd(90)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(100)
rturn()
t.fd(100)
t.lt(90)
t.fd(100)

t.lt(90)
t.fd(90)
rturn()
t.fd(90)
t.lt(90)
t.fd(100)

t.lt(90)
t.fd(100)
rturn()
t.fd(211)
rturn()
t.fd(100)
t.lt(90)
t.fd(100)

t.lt(90)
t.fd(90)
rturn()
t.fd(90)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
rturn()
t.fd(100)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(90)
for i in range(9):
    t.rt(10)
    t.fd(1)
for i in range(9):
    t.fd(1)
    t.lt(10)
t.fd(106)
t.fillcolor("red")
t.end_fill()
t.up()
t.done()
