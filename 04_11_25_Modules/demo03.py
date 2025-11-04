# from turtle import color, forward, right 
from turtle import * # --> everything from turtle module will be imported
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)