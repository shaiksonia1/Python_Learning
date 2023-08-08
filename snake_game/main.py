import pygame #importing a game module which is pygame used for graphics sounds display
from pygame.locals import*
#import time



if __name__ == "__main__":
    pygame.init() # we are initilaizing the pygame module

    surface = pygame.display.set_mode((1000,500)) #we are creating a display for our game by using pygame module using setmode function the width and height
    pygame.display.flip() #we are displaying the screen by calling this method it will only display for a second to keep it we need to use time.
    #time.sleep(5) # we are setting display time for 5 seconds


running = True


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pass
        elif event.type == QUIT:
            running = False
             