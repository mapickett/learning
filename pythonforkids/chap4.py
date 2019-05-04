
import turtle

#1: A Rectangle

t = turtle.Pen()
t.reset ()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

#2: A Triangle
t.reset()
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)


#3: A Box Without Corners
t.reset()
# First Side
t.up()
t.forward(10)
t.down()
t.forward(30)
t.up()
t.forward(10)

# Second side
t.left(90)
t.forward(10)
t.down()
t.forward(30)
t.up()
t.forward(10)

# Third side
t.left(90)
t.forward(10)
t.down()
t.forward(30)
t.up()
t.forward(10)

# Fourth side
t.left(90)
t.forward(10)
t.down()
t.forward(30)
t.up()
t.forward(10)


