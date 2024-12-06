import pygame as pg
# initialize pygame
pg.init() # imp to add this line else nothing gonna work

screen = pg.display.set_mode((400,300)) #creates screen; rmr to add tuple then add dimensions

# title and icon
pg.display.set_caption("teri mummy")
icon = pg.image.load("girl.png")
pg.display.set_icon(icon)

# adding image
block_img = pg.image.load("box.png")


def blocks(x,y):
    screen.blit(block_img,(x,y))

blockX = 0; blockY = 0

# game loop
running = True
while running:
    screen.fill((151,131,116))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # if keystroke is pressed check whether it's right or left
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:

 
    blocks(blockX,blockY)
    
    pg.display.update()
   