import turtle
from math import pi, sin, cos, fabs

angle=float(input("Enter angle with horizontal at which ball is thrown (degrees): "))
angle*=pi/180

speed=float(input("Enter speed with which ball is thrown (assume m/s): "))
gravity = -0.5
friction_speed_loss = -0.01
speed_loss = 0.8
drag_coeff = 0.0008
width = 1000
height = 600

y_velocity = speed*sin(angle)
x_velocity = speed*cos(angle)

go_x=True
go_y=True

window = turtle.Screen()
window.setup(width+40, height+40)
window.tracer(0)

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while go_x or go_y:
    
    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    
    if go_y:
        y_velocity += gravity
        if y_velocity>0:
            y_velocity-=drag_coeff*(y_velocity**2)
            
        elif y_velocity<0:
            y_velocity+=drag_coeff*(y_velocity**2)
            
        if ball.ycor()>(height/2):
            y_velocity = -y_velocity*speed_loss
            ball.sety(height/2)
            
        if ball.ycor()<(-height/2):
            y_velocity=-y_velocity*speed_loss
            ball.sety(-height/2)
            if fabs(y_velocity)<=4:
                y_velocity=0
                go_y=False
    if go_x:
        if x_velocity>0:
            x_velocity-=drag_coeff*(x_velocity**2)
            
        elif x_velocity<0:
            x_velocity+=drag_coeff*(x_velocity**2)
            
        if not go_y:
            if x_velocity>0:
                x_velocity+=friction_speed_loss
            elif x_velocity<0:
                x_velocity-=friction_speed_loss
                
        if ball.xcor()>(width/2):
            x_velocity = -x_velocity*speed_loss
            ball.setx(width/2)
                
        if ball.xcor()<-width/2:
            x_velocity = -x_velocity*speed_loss
            ball.setx(-width/2)
            
        if fabs(x_velocity)<=0.3:
                x_velocity=0
                go_x=False

    window.update()
