import turtle
import random
import time
import json

try:
    with open('highscore') as f:
        d=json.load(f)
    he=d['he']
    hn=d['hn']
    hh=d['hh']
    print('hello')
except Exception:
    d={'he':0, 'hn':0, 'hh':0}
    he=hn=hh=0
    
turtle.tracer(0)
global tails
tails=[]

global score
score=0

global highscore
highscore=0

Hard=turtle.textinput('Hardness','Easy or Normal or Hard')
if Hard.lower() in ['easy','normal','hard']:
    if Hard.lower()=='hard':
        sleep=0.06
        highscore=hh
    elif Hard.lower()=='normal':
        sleep=0.08
        highscore=hn
    else:
        sleep=0.09
        highscore=he
else:
    sleep=0.08
    highscore=hn
    
turtle.setup(width=900,height=900)   
turtle.screensize(600,600)
cornx,corny=300,300
turtle.bgcolor('black')
head=turtle.Turtle()
food=turtle.Turtle()
food.up()
food.shape('circle')
food.color('red')
food.speed(1)
food.goto(random.randint(-100,100),random.randint(-100,100))
head.up()
head.shape('square')
head.color('green')
head.speed(1)
writer=turtle.Turtle()
writer.ht()
writer.color('grey')
writer.up()
writer.goto(308,308)
writer.right(180)
writer.down()

def game_end():
    writer.color('Orange')
    writer.up()
    writer.goto(-60,0)
    writer.write('Game Over', font=("Arial", 30, "normal"))
    
def afterclear():
    writer.up()
    writer.goto(308,308)
    writer.seth(180)
    writer.down()
    for i in range(4):
        writer.forward(616)
        writer.left(90)

    writer.up()
    writer.goto(-200,-380)
    writer.write(f"Highscore : {highscore}   Score : {score}", font=("Arial", 20, "normal"))
    
afterclear()

def right():
    head.right(90)
    turtle.update()

def left():
    head.left(90)
    turtle.update()

turtle.onkeypress(right,'Right')
turtle.onkeypress(left,'Left')
turtle.listen()

play=True
while play:
    perp=head.pos()
    head.forward(22)
    distance=head.distance(food)
    if distance<20:
        food.goto(random.randint(-100,100),random.randint(-100,100))
        tail=turtle.Turtle()
        tail.up()
        tail.shape('square')
        tail.color('grey')
        tails.append(tail)
        score+=10
        if score>highscore:
            highscore=score
        writer.clear()
        afterclear()

    for i in range(len(tails)-1,0,-1):
        tails[i].goto(tails[i-1].pos())

    if len(tails)>0:
        tails[0].goto(perp)

    t_dist=[head.distance(i) for i in tails]
    if t_dist:
        if min(t_dist)<21.9 or (min(t_dist)==22 and len(tails)==1 and (x>=cornx or x<=-cornx or y>=corny or y<=-corny)):
            play=False
        
    x=head.xcor()
    y=head.ycor()
    
    if x>=cornx or x<=-cornx or y>=corny or y<=-corny:
        play=False

    time.sleep(sleep)
    turtle.update()
    
else:
    game_end()
    if Hard.lower()=='hard':
        if hh<highscore:
            d['hh']=highscore
    elif Hard.lower()=='normal':
        if hn<highscore:
            d['hn']=highscore
    else:
        if he<highscore:
            d['he']=highscore

with open('highscore','w') as f:
    json.dump(d,f)
