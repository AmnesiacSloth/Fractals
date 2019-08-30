import turtle 
# names anonymous turtle
chris = turtle.Turtle()
chris.speed(1)


def snowflakeside(sidelength, levels):
    ''' recursive function that will build one side of triangle '''
    # base case
    if levels == 0:
        chris.forward(sidelength)
        return
    # recurses by calling on itself
    else:
            snowflakeside(sidelength/3, levels-1)
            chris.left(60)
            snowflakeside(sidelength/3, levels-1)
            chris.right(120)
            snowflakeside(sidelength/3, levels-1)
            chris.left(60)
            snowflakeside(sidelength/3, levels -1)

# Main function
def snowFractal(sidelength,levels):
       ''' Turns turtle so that the snowflake can form '''
       snowflakeside(sidelength,levels)
       chris.right(120)
       snowflakeside(sidelength,levels)
       chris.right(120)
       snowflakeside(sidelength,levels)
       return

snowFractal(100,3)
turtle.done()
