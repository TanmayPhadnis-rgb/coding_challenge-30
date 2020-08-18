# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:25:14 2020

@author: TANMAY
"""

import pygame

# Variables

WIDTH = 1200
HEIGHT = 600
BORDER = 30
VELOCITY = 1
FRAMERATE = 260

# Define Classes

class Ball:
    RADIUS = 20
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)
        
    def update(self, colour):
        global bgColor, BallColor
        newx = self.x + self.vx
        newy = self.y + self.vy
       
        if newx < BORDER+self.RADIUS:
           self.vx = -self.vx
         
        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
            
        elif newx + Ball.RADIUS > WIDTH - Paddle.WIDTH and abs(newy - paddle.y) < Paddle.HEIGHT//2:
            self.vx = - self.vx
            
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(BallColor)
        
        
class Paddle:
    WIDTH = 20
    HEIGHT = 100
    
    def __init__(self, y):
        self.y = y
        
    def show(self, colour):
        global screen
        pygame.draw.rect(screen, colour, pygame.Rect(WIDTH-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))
        
    def update(self):
        self.show(pygame.Color("black"))
        self.y = pygame.mouse.get_pos()[1]
        self.show(pygame.Color("blue"))


# Create Objects
ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)
    

# Draw the Scenario

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

fgColor = pygame.Color("green")
bgColor = pygame.Color("black")
BallColor = pygame.Color("red")

pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (WIDTH, BORDER)))

pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, HEIGHT))

pygame.draw.rect(screen, fgColor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))


paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

ballplay.show(BallColor)

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    
    # visualize the changes you just made
    pygame.display.flip()
    
    paddle.update()
    ballplay.update(BallColor)

pygame.quit()