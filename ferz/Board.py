import turtle as t

class Board:
    def __init__(self, speed=2000, size=50, N=8):
        self.speed = speed
        t.speed(speed)
        self.SIZE = size
        self.N = N

    def ferz(self, j, k):
        x=j*self.SIZE-4*self.SIZE
        y=k*self.SIZE-4*self.SIZE #функция рисования ферзя
        if (j+k)%2==1: #смена цвета ферзя из-за клеток
            t.pencolor('white') #функция смены цвета
        self.rectangle(x,y,self.SIZE, True)
        self.rectangle(x,y,self.SIZE*0.67, False)
        self.trapec(x,y)
        self.korona(x,y)
        t.pencolor('black') #опять смена цвета

    def rectangle(self, x,y, size,check): #функция рисования прямоугольника внутри ферзя
        t.penup()
        if check:
            t.goto(self.SIZE/5+x, self.SIZE*0.18+y)
        else:
            t.goto(0.3*self.SIZE+x,0.31625*self.SIZE+y)
        t.pendown()
        for i in range(2):
            t.forward(size*0.6)
            t.left(90)
            t.forward(size/8)
            t.left(90)
        
    def trapec(self,x,y): #трапецию под короной
        t.penup()
        t.goto(self.SIZE*0.3+x, self.SIZE*0.4+y)
        t.pendown()
        t.goto(self.SIZE/5+x, self.SIZE/2+y)
        t.fd(0.6*self.SIZE)
        t.goto(self.SIZE*0.7+x, self.SIZE*0.4+y)
    

    def korona(self,x,y): #корона 
        t.penup()
        t.goto(self.SIZE/5+x, self.SIZE/2+y)
        t.pendown()
        t.goto(self.SIZE/10+x,self.SIZE*0.9+y)
        t.goto(self.SIZE*0.4+x, self.SIZE/2+y)
        t.goto(self.SIZE/2+x, self.SIZE*0.9+y)
        t.goto(self.SIZE*0.6+x, self.SIZE/2+y)
        t.goto(self.SIZE*0.9+x, self.SIZE*0.9+y)
        t.goto(self.SIZE*0.8+x, self.SIZE/2+y)
        
            
    def square(self,x,y,z): #клетки доски
        t.penup()
        t.goto(x,y)
        t.pendown()
        if z%2==1: #Сменя цвета относительно номера клетки
            t.fillcolor('black')
        else:
            t.fillcolor('white')
        t.begin_fill()
        for i in range(4):
            t.forward(self.SIZE)
            t.left(90)
        t.end_fill()

    def getN(self):
        return self.N

    def getSize(self):
        return self.SIZE
