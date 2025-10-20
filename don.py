import turtle 
import random


def draw_something(mouse_x, mouse_y):
    global tula
    x = round(mouse_x, 0)
    y = round(mouse_y, 0)
    print(f'TESTING: x={mouse_x}, y={mouse_y}')
    if x > 0 and x < 202:
        tula.color(get_random_colour())
        tula.penup()
        tula.goto(x, y)
        tula.pendown()
        tula.circle(20)

    #WHAT WILL YOUR CONDITIONAL PRODUCE?


def get_random_colour():

    c = (random.randint(0, 255), \
random.randint(0, 255), \
random.randint(0, 255))

    return c



    
def main():
    global tula
    
    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0, 0, 400, 400)
    world.colormode(255)
    world.bgcolor("white")

    tula = turtle.Turtle()
    tula.speed(10)
    tula.width(5)

    
    

    world.onclick(draw_something)
    
    
        
main()




