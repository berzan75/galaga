import pgzrun
import random

WIDTH=800
HEIGHT=450

ship=Actor("ship")
bug=Actor("bug")

score=0

ship.pos= (400,850 )

bullet=[]
enemies=[]

def draw():
    screen.blit("galaxy.jpg",(0,0))



pgzrun.go()