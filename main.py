

#imports the needed files
import pygame
import os
#inisilase pygame
pygame.init()

#defines all of the variables
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 44
WINDOW, HEIGHT = 900,500
screen = pygame.display.set_mode((WINDOW,HEIGHT))
pygame. display.set_caption("pygame game")
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
vel = 5
x= WINDOW/2-5
BORDER = pygame.Rect(x,0,10,HEIGHT)
red_bullets = []
yellow_bullets = []
BULLET_VEL = 7
num_bullets = 7
#all of the images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
SPACE_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

#creates the window
def draw_window(red:int, yellow:int):
    screen.fill((WHITE))
    #loads the images
    pygame.draw.rect(screen, BLACK, BORDER)
    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()

#movment scripts
def yellow_handlement_movement(key, yellow):
        
        if key[pygame.K_a] and yellow.x - vel > 0: #LEFT
            yellow.x -= vel
        if key[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x: #RIGHT
            yellow.x += vel
        if key[pygame.K_w] and yellow.y - vel > 0: #UP
            yellow.y -= vel
        if key[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT-15: #DOWN
            yellow.y += vel
def red_handlement_movement(key, red):
        
        if key[pygame.K_LEFT]and red.x - vel > BORDER.x +BORDER.width: #LEFT
            red.x -= vel
        if key[pygame.K_RIGHT]and red.x + vel + red.width < WINDOW: #RIGHT
            red.x += vel
        if key[pygame.K_UP] and red.y - vel > 0: #UP
            red.y -= vel
        if key[pygame.K_DOWN]and red.y + vel + red.height < HEIGHT-15: #DOWN
            red.y += vel

#main function
def main():
    # creates the squares
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #fireing the buttlets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < num_bullets:
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y+yellow.height/2 - 2, 10,5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < num_bullets:
                    bullet = pygame.Rect(red.x, red.y+red.height/2 - 2, 10,5)
                    yellow_bullets.append(bullet)
        print(red_bullets, yellow_bullets)
        key_pressed = pygame.key.get_pressed()
        yellow_handlement_movement(key_pressed,yellow)
        red_handlement_movement(key_pressed,red)
        draw_window(red,yellow)

        



    pygame.quit()

if __name__ == "__main__":
    main()