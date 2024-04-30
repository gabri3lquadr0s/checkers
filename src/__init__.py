from classesBoard import *
import turtle

t = turtle.Turtle()
sc = turtle.Screen()

brd = Board()
matrix = brd.draw('white','black', 48)
sc.mainloop()
print(matrix)

