import turtle
import math
from turtle import Turtle

turtle.setup(1000, 700)

screen_height = turtle.window_height()
screen_width = turtle.window_width()

class Ball(Turtle):
  def __init__(self, x, y, radius, color):
    Turtle.__init__(self)
    self.penup()
    self.setx(x)
    self.sety(y)
    self.vx = 0
    self.vy = 0
    self.color(color)
    self.shape("circle")
    self.radius = radius
    self.shapesize(radius/5)
  
  def set_velocity(self):
    canvas = turtle.getcanvas()
    mouse_x, mouse_y = canvas.winfo_pointerxy()
    mouse_x -= screen_width
    mouse_y *= -1
    mouse_y -= screen_height
    print(mouse_x, mouse_y)
    self.vx *= 1 * sigmoid(mouse_x - self.xcor())
    self.vy *= 1 * sigmoid(mouse_y - self.ycor())
  
  def move(self):
    my_x = self.xcor()
    my_y = self.ycor()

    self.set_velocity()

    if my_x + self.radius >= screen_width / 2 or my_x - self.radius <= -screen_width / 2:
      self.vx *= -1
    if my_y + self.radius >= screen_height / 2 or my_y - self.radius <= -screen_height / 2:
      self.vy *= -1

    self.setx(my_x + self.vx)
    self.sety(my_y + self.vy)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

ball = Ball(0,0, 10, "Red")

while(True):
  ball.move()

turtle.mainloop()