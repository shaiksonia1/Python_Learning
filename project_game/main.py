import pygame #first we will install a pygame module, pygame module used for creating games it consists of computer graphic and sounds
import sys




#next we are initilazing the pygame
pygame.init()
#we are setting the screen here foor display width and height by using setmode
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()


class Apple:
    def __init__(self,image,position,speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y +=self.speed


#constants
TILESIZE = 32

#floor

floor_image = pygame.image.load('project_game/assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image,(TILESIZE*15,TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0,screen.get_height()))


#player
player_image = pygame.image.load('project_game/assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image,(TILESIZE,TILESIZE*2))
player_rect  = player_image.get_rect(center=(screen.get_width()/2,
                                             screen.get_height()-floor_image.get_height()-(player_image.get_height()/2)))

#apple
apple_image = pygame.image.load('project_game/assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image,(TILESIZE,TILESIZE))

apples = [
    Apple(apple_image,(100,0),3),
    Apple(apple_image,(300,0),3),
]


running = True

def update():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 8
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 8

#apples management

for apple in apples:
    apple.move()

def draw():
    screen.fill('light blue')
    screen.blit(floor_image,floor_rect)
    screen.blit(player_image,player_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)



#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    
    
    
    update()
    draw()
    clock.tick(60)
    pygame.display.update()