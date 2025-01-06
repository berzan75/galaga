import pgzrun
import random

WIDTH=800
HEIGHT=450

ship=Actor("ship")
bug=Actor("bug")

score=0

ship.pos= (400,450 )

bullets=[]
enemies=[]

enemies.append(Actor("bug"))
enemies[-1].x=100
enemies[-1].y=-10

def draw():
    screen.blit("galaxy.jpg",(0,0))
    for bullet in bullets: 
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    display_score()
    
def display_score():
    screen.draw.text(str(score), (10,20))

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-10

def update():
    global score
    if keyboard.left:
        ship.x -=5
        if ship.x<=0:
            ship.x=0


    if keyboard.right:
        ship.x+=5
        if ship.x>=WIDTH:
            ship.x=WIDTH

    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else: 
            bullet.y-=10
    for enemy in enemies:
        enemy.y+=5
        if enemy.y>HEIGHT:
            enemy.y= -100
            enemy.x=random.randint(50, 750)

    for bullet in bullets:
        if enemy.colliderect(bullet):
            enemies.remove(enemy)
            bullets.remove(bullet)
            score= score +100


