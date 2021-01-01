import turtle

#draw the playground 
playground = turtle.Screen()
playground.bgcolor("yellow")
playground.title("Bat and Ball Game")
playground.setup(width=800, height=600, startx=0,starty=0)
#playground.tracer(0)

#score 
score_a=0
score_b=0

#draw the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1,1)
ball.penup()
ball.goto(0,0)
ball.moveX = 2
ball.moveY = -2

#draw the first bat 
bat_1 = turtle.Turtle()
bat_1.speed(0)
bat_1.shape("square")
bat_1.color("blue")
bat_1.shapesize(stretch_len=1, stretch_wid=5)
bat_1.penup()
bat_1.goto(-350,0)

#draw the second bat 
bat_2 = turtle.Turtle()
bat_2.speed(0)
bat_2.shape("square")
bat_2.color("green")
bat_2.shapesize(stretch_len=1, stretch_wid=5)
bat_2.penup()
bat_2.goto(350,0)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0  ", align="center", font=("Courior", 24, "normal") )

#move bat_1 
def mov_bat_1_up():
    y_movement = bat_1.ycor()
    y_movement += 20
    bat_1.sety(y_movement)

def mov_bat_1_down():
    y_movement = bat_1.ycor()
    y_movement -= 20
    bat_1.sety(y_movement)

#move bat_2 
def mov_bat_2_up():
    y_movement = bat_2.ycor()
    y_movement += 20
    bat_2.sety(y_movement)

def mov_bat_2_down():
    y_movement = bat_2.ycor()
    y_movement -= 20
    bat_2.sety(y_movement)

#keyboard binding 
playground.listen()
playground.onkeypress(mov_bat_1_up, "q")
playground.onkeypress(mov_bat_1_down, "z")
playground.onkeypress(mov_bat_2_up, "Up")
playground.onkeypress(mov_bat_2_down, "Down")




while True: 
    playground.update()

    #move the ball 
    ball.setx(ball.xcor() + ball.moveX )
    ball.sety(ball.ycor() + ball.moveY)

    #check the border 
    if (ball.ycor()> 290): 
        ball.sety(290)
        ball.moveY = ball.moveY*(-1)
    
    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.moveY = ball.moveY*(-1)
    
    
    if (ball.xcor()>390):
        ball.setx(390)
        ball.moveX = ball.moveX*(-1)
        score_a +=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}  ".format(score_b, score_b), align="center", font=("Courior", 24, "normal") )

    if (ball.xcor()<-390):
        ball.setx(-390)
        ball.moveX = ball.moveX*(-1)
        score_b +=1 
        pen.clear()
        pen.write("Player A: {}   Player B: {}  ".format(score_a, score_b), align="center", font=("Courior", 24, "normal") )

    #ball and bat collision 
    
    if((ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < bat_2.ycor()+ 40 and ball.ycor()> bat_2.ycor()-40)): 
       ball.setx(340)
       ball.moveX = ball.moveX*(-1)
    
    if((ball.xcor()< -340 and ball.xcor()>-350) and (ball.ycor() < bat_2.ycor()+ 40 and ball.ycor()> bat_2.ycor()-40)): 
       ball.setx(-340)
       ball.moveX = ball.moveX*(-1)

   

