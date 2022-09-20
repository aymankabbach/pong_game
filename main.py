from shutil import move
from turtle import Screen, exitonclick, onkey 
import time
from pong_classes import wall,paddle,ball,scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.title("pong game")
my_wall=wall()
second_paddle=paddle()
first_paddle=paddle()
my_ball=ball()
my_score=scoreboard()
EndoftheGame=False
screen.listen()
screen.onkey(second_paddle.Up,"Up")
screen.onkey(second_paddle.down,"Down")
screen.onkey(first_paddle.Up,"u")
screen.onkey(first_paddle.down,"d")
def start_game():
    global EndoftheGame
    screen.tracer(0)
    my_score.write_score()
    my_wall.draw_wall()
    second_paddle.setposition(-380,0)
    first_paddle.setposition(380,0)
    screen.update()
    while EndoftheGame==False:
        screen.tracer(0)
        my_ball.move_forward()
        my_score.check_goal(my_ball)
        my_wall.check_collosion_wall(my_ball)
        first_paddle.check_collosion_paddle(my_ball)
        second_paddle.check_collosion_paddle(my_ball)
        EndoftheGame=my_score.check_win()
        time.sleep(0.1)
        screen.update()
start_game()
exitonclick()