import pygame
import numpy as np
import Control as c

# initialising the window. You can ignore this part.

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 40)

# setting plate parameters

centerX = 400
centerY = 400
plateT = 60

r = 0.1 # the radius of the ball

# loading in images and transforming them to required sixes and angles. You can ignore this part.

plate = pygame.image.load("plate.png")
plate = pygame.transform.rotate(plate, -45)
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (40, 40))
pivot = pygame.image.load("plain-triangle.png")

# game control variable. This variable determines if the came continues to run. You can ignore this part.

run = True


# A function used to rotate an image about its center. You can ignore this part.
def blit_rot_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# initialising game parameters

theta = np.zeros(1001)     # the variable stores the angle of the plate with the
                # horizontal and measured positive counterclockwise.

phi = 0         # the variable stores the angle of rotation
                # of the ball about its own axis.

x = 0           # the variable stores the distance of
                # the center of the ball form the pivot.
sp_x = np.zeros(1001)

dtheta = np.zeros(1001)

j = 1

# Game loop
while run:
    i = 0
    # checking for mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                X, Y = event.pos  # gets the x and y coordinates of the mouse left click
                sp_x[i] = X - 400
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                X, Y = event.pos  # gets the x and y coordinates of the mouse left click and moving.
                sp_x[i] = X - 400

    # This is your major task. Write a function which takes in
    # any number of parameters you like and output the new system
    # variables and any other parameter you would like to track.
    theta[j] = c.PIDLoop(x , sp_x[i])  
    
    if theta[j] >= 15:
        theta[j] = 15
        
    if theta[j] <= -15:
        theta[j] = -15
    
    
    dtheta[j] = theta[j] - theta[j-1] 
    if dtheta[j] >= 1:
        dtheta[j] = 1
        
    if dtheta[j] <= -1:
        dtheta[j] = -1
        
    theta[j] = theta[j-1] + dtheta[j]
    
    dx = c.solve(theta[j])
    

    # make sure the ball rotates
    dphi = dx[-1][0] / r
    phi += dphi
    
    x += dx[-1][0]
    
    if x >= 300:
        x = 300
        
    if x <= -300:
        x = -300
        
    

    # setting the background colour of the screen
    screen.fill((235, 62, 74))

    # displaying the images on the screen within appropriate physical parameters,
    # for example, it is ensured that the ball is always on the plate.

    blit_rot_center(screen, plate, (centerX - 364, centerY - 364), theta[j])
    blit_rot_center(screen, ball, (centerX - 20 + x * np.cos(np.radians(theta[j])) - plateT * np.sin(np.radians(theta[j])),
                                   centerY - 20 - plateT * np.cos(np.radians(theta[j])) - x * np.sin(np.radians(theta[j]))),
                    -phi)
    screen.blit(pivot, (centerX - 32, centerY - 32 + plateT))

    pygame.display.update()
    
    i += 1
    j += 1
