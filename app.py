#import turtle module!
import turtle

#creates the screen object!
wind = turtle.Screen() 
wind.title("Welcome to Ping Pong game!") # set title to my window!
wind.bgcolor("black") #Backgroud color to the window
wind.setup(width=800 , height= 600)  #setting height and width to my window!

#window wont update by its own! it stops the window from updating automatically
wind.tracer(0)

 # Paddle1 :
paddle1 = turtle.Turtle() #inializes turtle object (shape) !
paddle1.speed(0) #setting speed to the fastest which is zero
paddle1.shape("square") # set the shape of object defualt 20 pix
paddle1.shapesize(stretch_wid= 5 , stretch_len=1) #stretches the shape to meet the size
paddle1.color("blue") #setthe color of the shape
paddle1.penup() #turtle will not draw anything!
paddle1.goto(-350,0)

# Paddle2 :
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square") #defualt 20 pix
paddle2.shapesize(stretch_wid= 5 , stretch_len=1)
paddle2.color("red")
paddle2.penup() #turtle will not draw anything!
paddle2.goto(350,0)

# Ball :

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") #defualt 20 pix
ball.color("white")
ball.penup() #turtle will not draw anything!
ball.goto(0,0)
ball.dx = 0.1 #the ball speed on the window! 
ball.dy = 0.1


#Score to know whois the winner:
score1 =0
score2 =0
score = turtle.Turtle()
score.speed(0)
score.color("pink")
score.penup()
score.hideturtle() # I dont need to see this object I just want to see the scores (Numbers)
score.goto(0,260)
score.write(" Player1: 0  player2 : 0 ", align="center", font=("Courier", 24,"normal"))


#Functions to move the paddles !

##PADDLE ONE :

def paddle1_up(): 
    y = paddle1.ycor() #get the y-coord of Paddle 1
    y+=20 # set y , increase it by 20
    paddle1.sety(y) #Update y tothe new y-coord!

def paddle1_down():
    y = paddle1.ycor() #get the y-coord of Paddle 1
    y-=20 # set y , decrease it by 20
    paddle1.sety(y) #Update y tothe new y-coord!

#Keyboard Bindings !
wind.listen()  
wind.onkeypress(paddle1_up,"q")  # when I press w Paddle one will move to up!
wind.onkeypress(paddle1_down,"a")  # when I press w Paddle one will move  down!

##PADDLE TWO :

def paddle2_up():
    y = paddle2.ycor()
    y+=20
    paddle2.sety(y) #Update y tothe new y-coord!

def paddle2_down():
    y = paddle2.ycor()
    y-=20
    paddle2.sety(y) #Update y tothe new y-coord!

#Keyboard Bindings !
wind.listen()  
wind.onkeypress(paddle2_up,"p")  # when I press w Paddle tow will move up!
wind.onkeypress(paddle2_down,"l")  # when I press w Paddle two will move down!
    
#Main game loop
while True:
    #Every time the loop works the window will be updated!
    wind.update()

    # MOving the ball!

    ball.setx(ball.xcor() + ball.dx)  #update the movement of theball
    #specify the place of the ball starts at zero, every time loops runs --> +2 on x axis
    # old place + 2.5 = new place !

    ball.sety(ball.ycor() +ball.dy) 


    # Border Check to the ball!  top border +300 px, bottom border -300 px , ball is 20 px

    # ball Hits up border:
    if ball.ycor() > 290: #if ball is at top border 
        ball.sety(290) #set y-coord  +290
        ball.dy *=-1 #reverse direction of ball , make +2.5 to -2.5

    # ball Hits down border :
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    #ball hits Right border :
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        score.clear()
        score.write(" Player1 :{}     player2 :{} ".format(score1,score2), align="center", font=("Courier", 24,"normal"))


    #ball hits letf border :   
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write(" Player1 :{}     player2 :{} ".format(score1,score2), align="center", font=("Courier", 24,"normal"))


# If ball hits one of paddles !
        
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40)  :
        ball.setx(340) 
        ball.dx *=-1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40)  :
        ball.setx(-340) 
        ball.dx *=-1    
     



   

