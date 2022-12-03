import turtle

ob1Dir = 0
ob2Dir = 0
ob3Dir = 0

def Up():
    y = turtle.ycor()
    y += 50
    turtle.sety(y)
    print("got it")

def Down():
    y = turtle.ycor()
    y += -50
    turtle.sety(y)
    print("got it")

def Right():
    x = turtle.xcor()
    x += 50
    turtle.setx(x)
    print("got it")
    

def Left():
    x = turtle.xcor()
    x-=50
    turtle.setx(x)
    print("got it")

 


def remake(ob):
    
    """this redraws the obsticles"""
    
    ob.fillcolor('red') 
    ob.begin_fill() 
    ob.circle(20)  
    ob.end_fill() 

def remake2(charac):
    
    charac.fillcolor('white') 
    charac.begin_fill() 
    charac.circle(20)  
    charac.end_fill()         
    
    


screen = turtle.Screen() 
screen.setup(500,500)    
screen.bgcolor('black')   
screen.tracer(0)  
         
obsticle1 = turtle.Turtle() 
obsticle1.color('red')
obsticle1.speed(0) 
obsticle1.width(2)     
obsticle1.hideturtle()          
obsticle1.penup()               
obsticle1.goto(-450,100) 
obsticle1.pendown() 

obsticle2 = turtle.Turtle() 
obsticle2.color('red')
obsticle2.speed(0) 
obsticle2.width(2)     
obsticle2.hideturtle()          
obsticle2.penup()               
obsticle2.goto(-450, 0) 
obsticle2.pendown()  

obsticle3 = turtle.Turtle() 
obsticle3.color('red')
obsticle3.speed(0) 
obsticle3.width(2)     
obsticle3.hideturtle()          
obsticle3.penup()               
obsticle3.goto(-450, 50) 
obsticle3.pendown()  

 
     
def updateCircles():
    
    """this updates the positiion of the obsticles"""
    
    global ob1Dir, ob2Dir, ob3Dir
    
    obsticle1.clear()  
    remake(obsticle1)  
    
    if obsticle1.pos()[0] <= -450:    
        ob1Dir = 1.5
    elif obsticle1.pos()[0] >= 450:
        ob1Dir = -1.1
    else:
        ob1Dir = ob1Dir
        
    obsticle1.forward(ob1Dir)
    
    
    
    
    obsticle2.clear()  
    remake(obsticle2)
    
    if obsticle2.pos()[0] <= -450:    
        ob2Dir = 3
    elif obsticle2.pos()[0] >= 450:
        ob2Dir = -1.5
    else:
        ob2Dir = ob2Dir
        
    obsticle2.forward(ob2Dir)
    
    
    
    obsticle3.clear()  
    remake(obsticle3)
    
    if obsticle3.pos()[0] <= -450:    
        ob3Dir = 4
    elif obsticle3.pos()[0] >= 450:
        ob3Dir = -2
    else:
        ob3Dir = ob3Dir
        
    obsticle3.forward(ob3Dir)
    
    
    
    
    
    
    screen.update()    
    
# infinite loop

  
turtle = turtle.Turtle()

turtle.color("green")

turtle.goto(-0, -250)



screen.onkey(Down(), "Down")    

screen.onkey(Left(), "Left")
screen.onkey(Up(), "Up")
screen.onkey(Right(), "Right")

screen.listen()

while True :
    
    
 
    
    updateCircles()
    turtle.clear()
    remake2(turtle)