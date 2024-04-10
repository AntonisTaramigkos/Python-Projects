import pygame
import random
# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invation")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)
background = pygame.image.load("BackGround_800x600.jpg")

# Player Variables
img_player = pygame.image.load("space-ship.png")
player_x = 368
player_y = 536
player_x_change = 0
player_y_change = 0

# Enemy Variables

img_enemy = pygame.image.load("alien.png")
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,200)
enemy_x_change = 0.3
enemy_y_change = 50

# Bullet Variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
visible_bullet = False

#Players Function
def player(x, y):
    screen.blit(img_player,(x, y))

#Enemy Function
def enemy(x, y):
    screen.blit(img_enemy,(x, y))

#Shoot Bullet
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x+24 , y+10))
    
# Game loop
is_running = True
while is_running:
    # RGB
    # BackGround Image
    screen.blit(background,(0,0))     

    #Event Iteration
    for event in pygame.event.get():

        # Close Key
        if event.type == pygame.QUIT:
            is_running = False
        #Press Key event
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
        #Release Key Event
        if event.type == pygame.KEYUP:
            if event.type ==pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0
            
    # Modify Player Loacation
    player_x += player_x_change    

    #Keep Player insde screen
    if player_x <=0:
        player_x = 0
    elif player_x >=736:
        player_x = 736

    # Modify Enemy Loacation
    enemy_x += enemy_x_change
    
    #Keep Enemy insde screen
    if enemy_x <=0:
        enemy_x_change = 0.8
        enemy_y += enemy_y_change
    elif enemy_x >=736:
        enemy_x_change = -0.8
        enemy_y += enemy_y_change

    # Bullets movment
    if bullet_y <= 16:
        bullet_y = 500
        visible_bullet = False

    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    #Update
    pygame.display.update()