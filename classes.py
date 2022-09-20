from turtle import Turtle
import random
angle=90
move_distance=20
d_x=""
d_y=""
x_y_pos=[-10,10]
direction_x=""
direction_y=""
class paddle(Turtle):
    def __init__(self):
        super().__init__()
    def setposition(self,x,y):
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)
    def Up(self):
        if self.ycor()<260:
            new_y=self.ycor()+move_distance
            self.goto(self.xcor(),new_y)
    def down(self):
        if self.ycor()>-260:
            new_y=self.ycor()-move_distance
            self.goto(self.xcor(),new_y)
    def check_collosion_paddle(self,bal):
        global d_x
        if (self.distance(bal)<50) and (bal.xcor()>=360 or bal.xcor()<-360):
            if d_x==1:
                d_x=0
            else:
                d_x=1
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize()
    def move_forward(self):
        global direction_x,direction_y,d_x,d_y,x_y_pos
        if d_x=="" and d_y=="":
            d_x=random.randint(0,1)
            d_y=random.randint(0,1)
            x=self.xcor()+x_y_pos[d_x]
            y=self.ycor()+x_y_pos[d_y]
        else:
            x=self.xcor()+x_y_pos[d_x]
            y=self.ycor()+x_y_pos[d_y]
        self.goto(x,y)
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score1=0
        self.score2=0
        self.setposition(x=0,y=320)
    def write_score(self):
        self.write(f"{self.score2} : {self.score1}",False,align="center",font=("Courier", 10, "normal"))
    def check_goal(self,bal,):
        global d_x,d_y
        if bal.xcor()>=400:
            self.score2+=1
            bal.goto(0,0)
            d_x=1
            d_y=random.randint(0,1)
        if bal.xcor()<=-400:
            self.score1+=1
            bal.goto(0,0)
            d_x=0
            d_y=random.randint(0,1)
        self.clear()
        self.write_score()
    def check_win(self):
        if self.score1==10:
            print("player 1 wins")
            return True
        if self.score2==10:
            print("player 2 wins")
            return True
        else:
            return False
class wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=-400,y=-310)
        self.pendown()
    def draw_wall(self):
        self.speed(10)
        for x in range(2):
            self.forward(800)
            self.left(angle)
            self.forward(620)
            self.left(angle)
    def check_collosion_wall(self,bal):
        global d_y
        if bal.ycor()>=300 or bal.ycor()<=-300:
            if d_y==0:
                d_y=1
            else:
                d_y=0