import turtle, time, pickle

with open('highscore.txt', 'rb') as file:
    highscore = pickle.load(file)
    
score = 0
timer = 5
clearscore = False
startgame = False

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Keepie Uppie │ SCORE: " + str(score) + " │ HIGHSCORE: " + str(highscore))
screen.screensize(400, 300)

write = turtle.Turtle()
write2 = turtle.Turtle()
write3 = turtle.Turtle()
writetitle = turtle.Turtle()
writetimer = turtle.Turtle()

writetitle.speed(0)
writetitle.hideturtle()
writetitle.penup()
writetitle.pencolor("white")
writetitle.goto(-230, -15)
writetitle.write("KEEPIE UPPIE", font=("FixedSys", 48, "normal"))
writetitle.penup()
writetitle.goto(-235, -20)
writetitle.pendown()
writetitle.forward(485)

time.sleep(5)
writetitle.clear()

write2.speed(0)
write2.hideturtle()
write2.penup()
write2.pencolor("white")
write2.goto(-465, 375)
write2.write("Press ESC to exit", font=("FixedSys", 16, "normal"))

write3.speed(0)
write3.pencolor("white")
write3.hideturtle()
write3.penup()
write3.goto(-465, 350)
write3.pendown()
write3.write("Press 1 to clear HIGHSCORE", font=("FixedSys", 16, "normal"))


box = turtle.Turtle()
box.pencolor("white")
box.hideturtle()
box.speed(0)
box.penup()
box.goto(-100, 100)
box.pendown()
for x in range(4):
    box.forward(200)
    box.right(90)
box.penup()

ball = turtle.Turtle()
ballX = 50
ballY = 0
ballDirX = 1
ballDirY = 1
ballspeed = 1
ball.penup()
ball.hideturtle()
ball.goto(ballX,ballY)
ball.showturtle()
ball.shape("circle")
ball.color("white")

bat = turtle.Turtle()
turtle.register_shape('bat.gif')
batX = 0
batY = -80
batDirX = 0
bat.penup()
bat.goto(batX,batY)
bat.shape("bat.gif")
bat.color("white")

def left():
    global batDirX
    batDirX = -1
     
def right():
    global batDirX
    batDirX = +1

def end():
    global endgame
    endgame = True

def test123():
    global clearscore
    clearscore = True
    
def writescore():
        write.speed(0)
        write.penup()
        write.hideturtle()
        write.goto(-106, 150)
        write.pencolor("white")
        write.pendown()
        write.write("GAME OVER", font=("FixedSys", 32, "normal"))
        write.penup()
        write.goto(-66, 120)
        write.pendown()
        write.write("SCORE: " + str(score), font=("FixedSys", 20, "normal"))

        write.speed(0)
        write.penup()
        write.hideturtle()
        write.goto(-66, -145)
        write.pencolor("white")
        write.pendown()
        write.write("Resetting... ", font=("FixedSys", 16, "normal"))
            
        writetimer.pencolor("white")
        writetimer.hideturtle()
        writetimer.penup()
        writetimer.goto(45, -145)
        writetimer.pendown()
        global timer
        while timer != 0:
            writetimer.clear()
            writetimer.write(str(timer), font=("FixedSys", 16, "normal"))
            timer = timer - 1
            time.sleep(1)
        write.clear()
        writetimer.clear()
clearscore = False
score = 0
with open('highscore.txt', 'rb') as file:
    highscore = pickle.load(file)
endgame = False

while endgame == False:

    screen.listen()
    screen.onkey(left,"Left")
    screen.onkey(right,"Right")
    screen.onkey(end,"Escape")
    screen.onkey(test123, "1")

    batX = batX + batDirX * 2
        
    if batX >= 85:
        batX = 85
        batDirX = 0
    if batX <= -85:
        batX = -85
        batDirX = 0

    bat.goto(batX,batY)
   
    ballX = ballX + ballDirX * ballspeed
    ballY = ballY + ballDirY * ballspeed

    if ballX >= 90:
        ballX = 90
        ballDirX = -ballDirX
    if ballX <= -90:
        ballX = -90
        ballDirX = -ballDirX      
    if ballY >= 90:
        ballY = 90
        ballDirY = -ballDirY
        score = score + 1
        write3.clear()
        write3.write("Press 1 to clear HIGHSCORE", font=("FixedSys", 16, "normal"))
        screen.title("Keepie Uppie │ Score: " + str(score) + " │ HIGHSCORE: " + str(highscore))
   
    if ballY <= -60 and ballX >= batX - 15 and ballX <= batX + 15:
        ballY = -60
        ballDirY = -ballDirY
        ballspeed = ballspeed + 1
  
    ball.goto(ballX,ballY)

    if ballY <= -90:
        ball.color("red")
        if score > highscore:
            highscore = score
            with open('highscore.txt', 'wb') as file:
                pickle.dump(highscore, file)
        screen.title("Keepie Uppie │ Score: " + str(score) + " │ HIGHSCORE: " + str(highscore))
        writescore()
        score = 0
        screen.title("Keepie Uppie │ Score: " + str(score) + " │ HIGHSCORE: " + str(highscore))
        ballX = 50
        ballY = 0
        ballDirX = 1
        ballDirY = 1
        ballspeed = 1
        ball.color("white")
        ball.hideturtle()
        ball.goto(ballX,ballY)
        ball.showturtle()
        batX = 0
        batY = -80
        bat.goto(batX,batY)
        timer = 5
        
    if clearscore == True:
        highscore = 0
        with open('highscore.txt', 'wb') as file:
            pickle.dump(highscore, file)
        write3.clear()
        write3.penup()
        write3.goto(-465, 350)
        write3.pendown()
        write3.write("Press 1 to clear HIGHSCORE // HIGHSCORE cleared!", font=("FixedSys", 16, "normal"))
        clearscore = False
        

screen.bye()
