import turtle
# name anonymous turtle
chris = turtle.Turtle()
chris.left(90)
def treefractal(length, height):
    ''' Draws a symetrical tree fractal with given parameters '''
    # base case
    if height == -1:
        return
    else: 
        chris.forward(length)
        chris.left(45)
        treefractal(length // 2, height - 1)
        chris.right(90)
        treefractal(length // 2, height - 1)
        chris.left(45)
        chris.backward(length)


treefractal(100, 5)
turtle.done()
