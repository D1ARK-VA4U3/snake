from turtle import *
from random import randrange
from freegames import square,vector

food=vecto(0,0)
sanke=[vector(10,0)]
aim=vector(0,-10)

def change(x,y):
  aim.x=x
  aim.y=y

def inside(head):
  return -200 <head.x <190 and -200

def move():
  head=snake[-1].copy()
  head.move(aim)
  
  if not inside(head) or head in snake:
    square(head.x,head.y,9,'red')
    update()
    return
  
  snake.append()
  
  if head==food:
    print('sanke',len(sanke))
    food.x=randrange(-15,15)*10
    food.y=randrange(-15,15)*10
    
  else:
    sanke.pop(0)
    
  clear()
  
  for body in snake:
    square(body.x,body.y,9,'green')
    
  square(food.x,food.y,9,'red')
  update()
  ontimer(move, 100)
  
  hideturtle()
  tracer(False)
  listen()
  onkey(lambda:changes(10.0),'Right')
  onkey(lambda:changes(-10.0),'left')
  onkey(lambda:change(0,10),'Up')
  onkey(lambda:changes(0,-10),'Down')
  
  move()
  done()
    