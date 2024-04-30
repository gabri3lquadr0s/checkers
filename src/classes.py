import turtle

t = turtle.Turtle()
sc = turtle.Screen()
control = 1

class Square:
    def __init__(self, color1, color2, size):
        self.color1 = color1
        self.color2 = color2
        self.size = size
        self.id = id(self)
    
    def draw(self):
        global control
        if control % 2 == 0: color = self.color1
        else: color = self.color2
        t.fillcolor(color)
        t.begin_fill() 

        pos = []
        for i in range(4): 
            t.forward(self.size) 
            t.left(90)
            pos.append(t.pos())
        t.forward(self.size) 
        t.end_fill()
        return({"color": color, "id": self.id, "pos": pos})
    


class Board:
    def __init__(self):
        self
    
    def draw(self, color1, color2, size):
        global control
        squaresInBoard = []
        sc.setup(600, 700)
        for i in range(8):
            t.speed(999)
            t.penup()
            t.setpos(-200, -48 * i) 
            t.pendown()

            for ii in range(8):
                square = Square(color1, color2, size)                
                newSqr = square.draw()
                squaresInBoard.append(newSqr)
                control += 1
            control += 1
        t.hideturtle()
        return squaresInBoard
    
    def click():
        asd=asd

class Piece:
    def __init__(self, color1, color2, size):
        self.color1
        self.color2

    


        